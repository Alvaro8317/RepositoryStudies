import aws_cdk
import constructs
from aws_cdk import (
    aws_s3 as s3,
)

from cdk import context
from cdk.resources import dynamodb, glue, streaming


class CdkStack(aws_cdk.Stack):
    def __init__(
        self, scope: constructs.Construct, construct_id: str, *, env_name: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "DeaCertificationBucket",
            bucket_name=f"alvaro8317-dea-certification-{env_name}",
        )

        # Toggle costly modules on/off via cdk.json context (or `-c enableX=true/false`)
        # without touching this file — resources removed this way get deleted on the
        # next `cdk deploy`, since they simply disappear from the synthesized template.
        if context.context_flag(self.node, context.ContextFlag.ENABLE_STREAMING, default=True):
            streaming.add_streaming_resources(self, env_name=env_name, bucket=bucket)

        if context.context_flag(self.node, context.ContextFlag.ENABLE_GLUE, default=True):
            glue.add_glue_resources(self, env_name=env_name, bucket=bucket)

        if context.context_flag(self.node, context.ContextFlag.ENABLE_DYNAMODB, default=True):
            dynamodb.add_dynamodb_resources(self, env_name=env_name)
