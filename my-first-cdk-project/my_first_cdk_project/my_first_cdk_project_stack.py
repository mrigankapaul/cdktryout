from aws_cdk import (aws_s3 as _s3, aws_iam as _iam, core)


class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name = "myfirstcdkproject-mp",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        myBucket = _s3.Bucket(
            self,
            "myBucketId1"
        )

        _iam.Group(self, "gid")

        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value = myBucket.bucket_name,
            description=f"My First CDK bucket",
            export_name="myBucketOutput1"
        )
