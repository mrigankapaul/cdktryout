from aws_cdk import (aws_s3 as _s3, core)


class MyArtifactBucketStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # to refer from cdk.json
        print(self.node.try_get_context('us')['account'])

        if is_prod:
            artifactBucket = _s3.Bucket(
                self, 
                "myProdArtifactBucketId", 
                versioned=True, 
                encryption=_s3.BucketEncryption.S3_MANAGED, 
                removal_policy=core.RemovalPolicy.RETAIN
                )
        else: 
            artifactBucket = _s3.Bucket(
                self,
                "myDevArtifactBucketId",
                removal_policy=core.RemovalPolicy.DESTROY
            )