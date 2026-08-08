import aws_cdk
import constructs
from aws_cdk import (
    aws_s3 as s3,
)

from cdk.resources.glue import add_glue_resources
from cdk.resources.streaming import add_streaming_resources


def _context_flag(node: constructs.Node, key: str, *, default: bool) -> bool:
    """Reads a boolean CDK context value from cdk.json / cdk.context.json / `-c key=value`.

    CLI-supplied context (`-c key=value`) always arrives as a string, so a plain
    truthiness check on `-c enableGlue=false` would wrongly evaluate to True.
    """
    value = node.try_get_context(key)
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


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
        if _context_flag(self.node, "enableStreaming", default=True):
            add_streaming_resources(self, env_name=env_name, bucket=bucket)

        if _context_flag(self.node, "enableGlue", default=True):
            add_glue_resources(self, env_name=env_name, bucket=bucket)
