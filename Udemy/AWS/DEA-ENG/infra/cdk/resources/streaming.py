import pathlib

import aws_cdk
import constructs
from aws_cdk import (
    aws_iam as iam,
)
from aws_cdk import (
    aws_kinesis as kinesis,
)
from aws_cdk import (
    aws_kinesisfirehose as firehose,
)
from aws_cdk import (
    aws_lambda as lambda_,
)
from aws_cdk import (
    aws_lambda_event_sources as lambda_event_sources,
)
from aws_cdk import (
    aws_s3 as s3,
)

LAMBDA_DIR = pathlib.Path(__file__).resolve().parent.parent / "lambda"


def add_streaming_resources(
    stack: constructs.Construct, *, env_name: str, bucket: s3.IBucket
) -> None:
    """Kinesis Data Stream, its Lambda consumer and the Firehose delivery stream
    (with its own transform Lambda) that reads from that same stream."""

    data_stream = kinesis.Stream(
        stack,
        "DataStream",
        stream_name=f"data-stream-{env_name}",
        stream_mode=kinesis.StreamMode.ON_DEMAND,
        # Kinesis streams default to RETAIN: without this, toggling the module off via
        # `enableStreaming` would orphan (not delete) the stream, and it would keep billing.
        removal_policy=aws_cdk.RemovalPolicy.DESTROY,
    )

    stream_consumer_role = iam.Role(
        stack,
        "StreamConsumerLambdaRole",
        role_name=f"stream-consumer-lambda-role-{env_name}",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),  # type: ignore[arg-type]
        managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "service-role/AWSLambdaBasicExecutionRole"
            ),
        ],
    )
    data_stream.grant_read(stream_consumer_role)
    bucket.grant_write(stream_consumer_role, "streaming-data/*")

    stream_consumer_function = lambda_.Function(
        stack,
        "StreamConsumerFunction",
        function_name=f"stream-consumer-{env_name}",
        role=stream_consumer_role,  # type: ignore[arg-type]
        runtime=lambda_.Runtime.PYTHON_3_12,
        handler="index.lambda_handler",
        code=lambda_.Code.from_asset(str(LAMBDA_DIR / "stream_consumer")),
        environment={
            "BUCKET_NAME": bucket.bucket_name,
        },
    )
    stream_consumer_function.add_event_source(
        lambda_event_sources.KinesisEventSource(
            data_stream,
            # Standard (shared-throughput) consumer, no enhanced fan-out consumer registered.
            starting_position=lambda_.StartingPosition.LATEST,
            batch_size=100,
        )
    )

    firehose_transform_function_role = iam.Role(
        stack,
        "FirehoseTransformFunctionRole",
        role_name=f"firehose-transform-function-role-{env_name}",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),  # type: ignore[arg-type]
        managed_policies=[
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "service-role/AWSLambdaBasicExecutionRole"
            ),
        ],
    )

    firehose_transform_function = lambda_.Function(
        stack,
        "FirehoseTransformFunction",
        function_name=f"firehose-transform-{env_name}",
        role=firehose_transform_function_role,  # type: ignore[arg-type]
        runtime=lambda_.Runtime.PYTHON_3_12,
        handler="index.lambda_handler",
        code=lambda_.Code.from_asset(str(LAMBDA_DIR / "firehose_transform")),
        timeout=aws_cdk.Duration.minutes(1),
    )

    firehose_role = iam.Role(
        stack,
        "FirehoseDeliveryRole",
        role_name=f"firehose-delivery-role-{env_name}",
        assumed_by=iam.ServicePrincipal("firehose.amazonaws.com"),  # type: ignore[arg-type]
    )
    kinesis_read_grant = data_stream.grant_read(firehose_role)
    s3_write_grant = bucket.grant_write(firehose_role, "firehose-streaming-cdk/*")
    invoke_grant = firehose_transform_function.grant_invoke(firehose_role)

    delivery_stream = firehose.CfnDeliveryStream(
        stack,
        "KdsToS3DeliveryStream",
        delivery_stream_name=f"kds-to-s3-{env_name}",
        delivery_stream_type="KinesisStreamAsSource",
        kinesis_stream_source_configuration=firehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
            kinesis_stream_arn=data_stream.stream_arn,
            role_arn=firehose_role.role_arn,
        ),
        extended_s3_destination_configuration=firehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
            bucket_arn=bucket.bucket_arn,
            role_arn=firehose_role.role_arn,
            prefix="firehose-streaming-cdk/",
            buffering_hints=firehose.CfnDeliveryStream.BufferingHintsProperty(
                size_in_m_bs=5,
                interval_in_seconds=300,
            ),
            processing_configuration=firehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                enabled=True,
                processors=[
                    firehose.CfnDeliveryStream.ProcessorProperty(
                        type="Lambda",
                        parameters=[
                            firehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="LambdaArn",
                                parameter_value=firehose_transform_function.function_arn,
                            ),
                        ],
                    ),
                ],
            ),
        ),
    )
    # IAM permissions are eventually consistent: force the grants' policies to be
    # created before Firehose tries to assume the role and use them.
    kinesis_read_grant.apply_before(delivery_stream)
    s3_write_grant.apply_before(delivery_stream)
    invoke_grant.apply_before(delivery_stream)
