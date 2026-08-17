import aws_cdk as cdk
from aws_cdk.assertions import Template

from cdk import cdk_stack


def _synth_template() -> Template:
    app = cdk.App()
    stack = cdk_stack.CdkStack(
        app,
        "test-stack",
        db_password="test-password-1234",
        my_ip="203.0.113.10",
    )
    return Template.from_stack(stack)


def test_rds_postgres_instance_created():
    template = _synth_template()

    template.has_resource_properties(
        "AWS::RDS::DBInstance",
        {
            "DBInstanceIdentifier": "db-postgres-warehouse",
            "DBInstanceClass": "db.t4g.micro",
            "Engine": "postgres",
            "AllocatedStorage": "20",
            "StorageType": "gp3",
            "MultiAZ": False,
            "PubliclyAccessible": True,
        },
    )


def test_security_group_restricts_postgres_to_dev_ip():
    template = _synth_template()

    template.has_resource_properties(
        "AWS::EC2::SecurityGroup",
        {
            "SecurityGroupIngress": [
                {
                    "CidrIp": "203.0.113.10/32",
                    "FromPort": 5432,
                    "ToPort": 5432,
                    "IpProtocol": "tcp",
                }
            ],
        },
    )
