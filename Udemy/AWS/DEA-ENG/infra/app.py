#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk.cdk_stack import CdkStack

app = cdk.App()
CdkStack(
    app,
    "aws-dea-course",
    # Cuenta y región se resuelven del profile "local" (definido en cdk.json)
    # que AWS CLI/CDK usan para poblar CDK_DEFAULT_ACCOUNT/CDK_DEFAULT_REGION.
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION", "us-east-1"),
    ),
)

app.synth()
