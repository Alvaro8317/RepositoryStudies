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

SCRIPTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "scripts"


def add_glue_resources(
    stack: constructs.Construct, *, env_name: str, bucket: s3.IBucket
) -> None:
    """Glue Data Catalog database, crawler over `documents/` and the ETL job that
    converts those documents to Parquet under `documents-target/`."""

    # Glue naming rules only allow lowercase letters, numbers and underscores.
    database_name = f"customers_{env_name}"

    database = glue.CfnDatabase(
        stack,
        "CustomersDatabase",
        catalog_id=aws_cdk.Stack.of(stack).account,
        database_input=glue.CfnDatabase.DatabaseInputProperty(
            name=database_name,
        ),
    )

    crawler_role = iam.Role(
        stack,
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
        stack,
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
        stack,
        "DocumentsToParquetScript",
        path=str(SCRIPTS_DIR / "documents_to_parquet.py"),
    )

    etl_job_role = iam.Role(
        stack,
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
        stack,
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
