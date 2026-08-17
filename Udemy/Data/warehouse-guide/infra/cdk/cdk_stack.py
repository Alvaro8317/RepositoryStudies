import aws_cdk as cdk
import constructs
from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
)


class CdkStack(cdk.Stack):
    def __init__(
        self,
        scope: constructs.Construct,
        construct_id: str,
        *,
        db_password: str,
        my_ip: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # No NAT gateways (they're not free-tier eligible): only public subnets, since
        # the instance needs to be reachable directly from a developer's machine.
        vpc = ec2.Vpc(
            self,
            "Vpc",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
            ],
        )

        db_security_group = ec2.SecurityGroup(
            self,
            "DbSecurityGroup",
            vpc=vpc,
            description="Allows PostgreSQL access to db-postgres-warehouse",
            allow_all_outbound=True,
        )
        db_security_group.add_ingress_rule(
            ec2.Peer.ipv4(f"{my_ip}/32"),
            ec2.Port.tcp(5432),
            "PostgreSQL access from the developer current IP",
        )

        rds.DatabaseInstance(
            self,
            "DbPostgresWarehouse",
            instance_identifier="db-postgres-warehouse",
            engine=rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_18_3),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T4G, ec2.InstanceSize.MICRO),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_groups=[db_security_group],
            publicly_accessible=True,
            # Default engine username ("postgres"); password comes from .env (see app.py)
            # instead of an auto-generated Secrets Manager secret, per course setup.
            credentials=rds.Credentials.from_password(
                "postgres", cdk.SecretValue.unsafe_plain_text(db_password)
            ),
            allocated_storage=20,
            storage_type=rds.StorageType.GP3,
            multi_az=False,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            deletion_protection=False,
        )
