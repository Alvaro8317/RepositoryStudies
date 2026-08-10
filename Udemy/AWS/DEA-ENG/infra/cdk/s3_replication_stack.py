import aws_cdk
import constructs
from aws_cdk import (
    aws_s3 as s3,
)


class S3ReplicationTargetStack(aws_cdk.Stack):
    """Destination bucket for Cross-Region Replication.

    Deployed on its own so it can live in a different region than
    S3ReplicationSourceStack — see `6-storage-s3/8-cross-region-replication.md`.
    """

    def __init__(self, scope: constructs.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.bucket = s3.Bucket(
            self,
            "TargetBucket",
            bucket_name="target-important-alvaro8317",
            # Replication requires versioning on both source and destination.
            versioned=True,
        )


class S3ReplicationSourceStack(aws_cdk.Stack):
    """Source bucket with a replication rule pointing at the bucket created by
    S3ReplicationTargetStack. CDK wires the replication role and the destination
    bucket policy automatically from `replication_rules`."""

    def __init__(
        self,
        scope: constructs.Construct,
        construct_id: str,
        *,
        target_bucket: s3.IBucket,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "SourceBucket",
            bucket_name="source-important-alvaro8317",
            versioned=True,
            replication_rules=[
                s3.ReplicationRule(
                    destination=target_bucket,
                    # Mirrors the console practice: delete markers stay
                    # unreplicated so CRR still protects against accidental
                    # deletes in the source bucket.
                    delete_marker_replication=False,
                    # CDK always emits a (possibly empty) Filter, which puts the
                    # rule on S3's V2 replication schema — that schema requires
                    # Priority to be set explicitly, or CloudFormation rejects it.
                    priority=1,
                )
            ],
        )
