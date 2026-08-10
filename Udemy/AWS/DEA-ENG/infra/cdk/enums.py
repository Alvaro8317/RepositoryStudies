from enum import Enum


class AwsRegion(str, Enum):
    """AWS regions actually used by this project's stacks."""

    US_EAST_1 = "us-east-1"
    US_WEST_2 = "us-west-2"


class Environment(str, Enum):
    """Deployment environments (`ENVIRONMENT` env var / `env_name` stack param)."""

    PROD = "prod"
