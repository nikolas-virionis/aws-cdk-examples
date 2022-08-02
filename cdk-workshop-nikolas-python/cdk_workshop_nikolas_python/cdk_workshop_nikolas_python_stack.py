from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as lambdaService,
    aws_s3 as s3
)


class CdkWorkshopNikolasPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaFunction = lambdaService.Function(
            scope=self,
            id='lambda-function-python',
            handler='main.lambda_handler',
            code=lambdaService.Code.from_asset('src'),
            runtime=lambdaService.Runtime.PYTHON_3_8,
            function_name='lambda-function-python'
        )

        bucket = s3.Bucket(
            scope=self,
            id='bucket-teste-python-workshop-cdk',
            bucket_name='bucket-teste-python-workshop-cdk'
        )

        bucket.grant_read_write(lambdaFunction)


