#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk import cdk_stack

app = cdk.App()
cdk_stack.CdkStack(
    app,
    "aws-dea-course",
    env_name=os.getenv("ENVIRONMENT", "prod"),
    # Cuenta y región se resuelven del profile "local" (definido en cdk.json)
    # que AWS CLI/CDK usan para poblar CDK_DEFAULT_ACCOUNT/CDK_DEFAULT_REGION.
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION", "us-east-1"),
    ),
)

app.synth()
