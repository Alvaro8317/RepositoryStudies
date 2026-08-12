import pathlib

import aws_cdk
import constructs
from aws_cdk import (
    aws_dynamodb as dynamodb,
)
from aws_cdk import (
    aws_iam as iam,
)
from aws_cdk import (
    aws_lambda as lambda_,
)
from aws_cdk import (
    aws_lambda_event_sources as lambda_event_sources,
)

LAMBDA_DIR = pathlib.Path(__file__).resolve().parent.parent / "lambda"


def add_dynamodb_resources(stack: constructs.Construct, *, env_name: str) -> None:
    """DynamoDB table with streams enabled, and a Lambda that consumes that stream
    to validate the trigger wiring (it just prints the received event)."""

    table = dynamodb.Table(
        stack,
        "ArticlesTable",
        table_name=f"articles-{env_name}",
        partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
        billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        stream=dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
        # Tables default to RETAIN: without this, toggling the module off via
        # `enableDynamodb` would orphan (not delete) the table on the next `cdk deploy`.
        removal_policy=aws_cdk.RemovalPolicy.DESTROY,
    )

    stream_processor_role = iam.Role(
        stack,
        "DynamodbStreamProcessorRole",
        role_name=f"dynamodb-stream-processor-role-{env_name}",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),  # type: ignore[arg-type]
        managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "service-role/AWSLambdaBasicExecutionRole"
            ),
        ],
    )
    # Grants exactly the four actions a stream consumer needs: GetRecords,
    # GetShardIterator, DescribeStream and ListStreams.
    table.grant_stream_read(stream_processor_role)

    stream_processor_function = lambda_.Function(
        stack,
        "DynamodbStreamProcessorFunction",
        function_name=f"dynamodb-stream-processor-{env_name}",
        role=stream_processor_role,  # type: ignore[arg-type]
        runtime=lambda_.Runtime.PYTHON_3_12,
        handler="index.lambda_handler",
        code=lambda_.Code.from_asset(str(LAMBDA_DIR / "dynamodb_stream_processor")),
    )
    stream_processor_function.add_event_source(
        lambda_event_sources.DynamoEventSource(
            table,
            starting_position=lambda_.StartingPosition.LATEST,
            batch_size=1,
        )
    )
