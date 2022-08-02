import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class CdkWorkshopNikolasStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const lambdaFunction = new lambda.Function(this, 'lambda-function', {
        runtime: lambda.Runtime.PYTHON_3_8,
        handler: 'main.lambda_handler',
        code: lambda.Code.fromAsset('src')
    })

    const bucket = new s3.Bucket(this, 'bucket1-nikolas-workshop-cdk', {
        bucketName: 'bucket1-nikolas-workshop-cdk'
    })

    bucket.grantRead(lambdaFunction)
  }
}
