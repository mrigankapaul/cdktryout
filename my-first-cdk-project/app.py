#!/usr/bin/env python3

from aws_cdk import core

from my_first_cdk_project.my_first_cdk_project_stack import MyArtifactBucketStack

app = core.App()

env_US = core.Environment(
    account=app.node.try_get_context('us')['account'], 
    region=app.node.try_get_context('us')['region']
)

env_DEFAULT = core.Environment(
    account=app.node.try_get_context('default')['account'], 
    region=app.node.try_get_context('default')['region']
)

MyArtifactBucketStack(app,"myDevStack",env=env_US)
MyArtifactBucketStack(app,"myProdStack",is_prod=True,env=env_DEFAULT)

app.synth()
