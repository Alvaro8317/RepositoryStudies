#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk import cdk_stack, context, enums, s3_replication_stack

app = cdk.App()

account = os.getenv("CDK_DEFAULT_ACCOUNT")
default_region = os.getenv("CDK_DEFAULT_REGION", enums.AwsRegion.US_EAST_1.value)

cdk_stack.CdkStack(
    app,
    "aws-dea-course",
    env_name=os.getenv("ENVIRONMENT", enums.Environment.PROD.value),
    # Cuenta y región se resuelven del profile "local" (definido en cdk.json)
    # que AWS CLI/CDK usan para poblar CDK_DEFAULT_ACCOUNT/CDK_DEFAULT_REGION.
    env=cdk.Environment(account=account, region=default_region),
)

# Separate pair of stacks (rather than added to CdkStack's resources/) because
# Cross-Region Replication genuinely needs two stacks in two different regions —
# see 6-storage-s3/8-cross-region-replication.md. cross_region_references lets the
# source stack reference the target bucket via CDK's SSM-backed cross-region export.
if context.context_flag(
    app.node, context.ContextFlag.ENABLE_S3_REPLICATION, default=True
):
    s3_replication_target = s3_replication_stack.S3ReplicationTargetStack(
        app,
        "s3-replication-target",
        env=cdk.Environment(account=account, region=enums.AwsRegion.US_WEST_2.value),
        cross_region_references=True,
    )
    s3_replication_stack.S3ReplicationSourceStack(
        app,
        "s3-replication-source",
        target_bucket=s3_replication_target.bucket,
        env=cdk.Environment(account=account, region=default_region),
        cross_region_references=True,
    )

app.synth()
