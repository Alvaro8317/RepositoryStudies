#!/usr/bin/env python3
import os
import urllib.request

import aws_cdk as cdk
from dotenv import load_dotenv

from cdk import cdk_stack

load_dotenv()

app = cdk.App()

db_password = os.environ["DB_PASSWORD"]

# The security group only allows PostgreSQL from this IP. Override with
# `-c myIp=x.x.x.x` if the automatic lookup fails or your IP changed since deploy.
my_ip = app.node.try_get_context("myIp")
if not my_ip:
    try:
        with urllib.request.urlopen("https://checkip.amazonaws.com", timeout=5) as response:
            my_ip = response.read().decode().strip()
    except OSError as error:
        raise RuntimeError(
            "Could not auto-detect your public IP for the DB security group. "
            "Pass it explicitly with: cdk deploy -c myIp=x.x.x.x"
        ) from error

account = os.getenv("CDK_DEFAULT_ACCOUNT")
region = os.getenv("CDK_DEFAULT_REGION", "us-east-1")

cdk_stack.CdkStack(
    app,
    "data-warehouse-guide-course",
    db_password=db_password,
    my_ip=my_ip,
    # Cuenta y región se resuelven del profile "local" (definido en cdk.json)
    # que AWS CLI/CDK usan para poblar CDK_DEFAULT_ACCOUNT/CDK_DEFAULT_REGION.
    env=cdk.Environment(account=account, region=region),
)

app.synth()
