from enum import Enum

import constructs


class ContextFlag(str, Enum):
    """Boolean toggles read from cdk.json / cdk.context.json / `-c key=value`."""

    ENABLE_STREAMING = "enableStreaming"
    ENABLE_GLUE = "enableGlue"
    ENABLE_S3_REPLICATION = "enableS3Replication"
    ENABLE_DYNAMODB = "enableDynamodb"


def context_flag(node: constructs.Node, key: ContextFlag, *, default: bool) -> bool:
    """Reads a boolean CDK context value from cdk.json / cdk.context.json / `-c key=value`.

    CLI-supplied context (`-c key=value`) always arrives as a string, so a plain
    truthiness check on `-c enableGlue=false` would wrongly evaluate to True.
    """
    value = node.try_get_context(key.value)
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"
