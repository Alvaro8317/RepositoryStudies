import pathlib

import aws_cdk
import constructs
from aws_cdk import (
    aws_glue as glue,
)
from aws_cdk import (
    aws_iam as iam,
)
from aws_cdk import (
    aws_s3 as s3,
)
from aws_cdk import (
    aws_s3_assets as s3_assets,
)

SCRIPTS_DIR = pathlib.Path(__file__).parent / "scripts"


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

        # Glue naming rules only allow lowercase letters, numbers and underscores.
        database_name = f"customers_{env_name}"

        database = glue.CfnDatabase(
            self,
            "CustomersDatabase",
            catalog_id=self.account,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name=database_name,
            ),
        )

        crawler_role = iam.Role(
            self,
            "CustomersCrawlerRole",
            role_name=f"customers-crawler-role-{env_name}",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),  # type: ignore[arg-type]
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSGlueServiceRole"
                ),
            ],
        )
        bucket.grant_read(crawler_role, "documents/*")

        crawler = glue.CfnCrawler(
            self,
            "CustomersCrawler",
            name=f"customers-crawler-{env_name}",
            role=crawler_role.role_arn,
            database_name=database_name,
            # No schedule => the crawler only runs on-demand.
            targets=glue.CfnCrawler.TargetsProperty(
                s3_targets=[
                    glue.CfnCrawler.S3TargetProperty(
                        # Trailing slash + default crawler behavior scans every subfolder.
                        path=f"s3://{bucket.bucket_name}/documents/",
                    ),
                ],
            ),
            table_prefix="cdk-table",
        )
        crawler.add_dependency(database)

        etl_script = s3_assets.Asset(
            self,
            "DocumentsToParquetScript",
            path=str(SCRIPTS_DIR / "documents_to_parquet.py"),
        )

        etl_job_role = iam.Role(
            self,
            "DocumentsToParquetJobRole",
            role_name=f"documents-to-parquet-job-role-{env_name}",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),  # type: ignore[arg-type]
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSGlueServiceRole"
                ),
            ],
        )
        bucket.grant_read(etl_job_role, "documents/*")
        bucket.grant_write(etl_job_role, "documents-target/*")
        etl_script.grant_read(etl_job_role)

        glue.CfnJob(
            self,
            "DocumentsToParquetJob",
            name=f"documents-to-parquet-{env_name}",
            role=etl_job_role.role_arn,
            glue_version="4.0",
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                script_location=etl_script.s3_object_url,
                python_version="3",
            ),
            default_arguments={
                "--job-language": "python",
                "--SOURCE_PATH": f"s3://{bucket.bucket_name}/documents/",
                "--TARGET_PATH": f"s3://{bucket.bucket_name}/documents-target/",
            },
            # No schedule => same on-demand-only convention as the crawler above.
            max_retries=0,
            number_of_workers=2,
            worker_type="G.1X",
        )
