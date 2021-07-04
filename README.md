# AWS Lambda with Docker image showroom

Showroom to demonstrate how to use Docker image with AWS Lambda
This Lambda function generate a book when invoked.

## Prerequisites

* [Serverless](https://www.serverless.com)
* An [AWS](https://console.aws.amazon.com/) account.

## Repository architecture

* src/ : technical source code
* [src/app.py](src/app.py) : Python script run by Docker image on AWS Lambda service.
* [src/Dockerfile](src/Dockerfile) : Docker sources.
* [src/Makefile](src/Makefile) : orchestrate build and test commands.
* [src/requirements.txt](src/requirements.txt) : Python script (src/app.py) dependencies.
* [src/serverless.yml](src/serverless.yml) : Serverless framework file.
* [pyproject.toml](pyproject.toml) : Python configuration.
* [pyrightconfig.json](pyrightconfig.json) : Python configuration.

## How to test

Tests are everything. Here's how to test.

### locally

As severless does not support local testing for Lambda with Docker, we created a Makefile step to emulate this behavior.
You can run command `cd src/ && make test` to :

* Build local image (name myonlinebookstore_lambda_book:latest)
* Run container from this image.

When the container is ready, your Lambda (running with Docker) will wait to be invoked. Open a new terminal and run `cd src/ && make run-test-query-local` :

```bash
MacbookPro-2:src jchauvet$ make run-test-query-local
{"statusCode": 200, "body": {"body": "{\"book\": {\"isbn\": \"978-0-10-886465-0\", \"title\": \"Chance keep candidate back all.\", \"author\": \"James Gonzalez\", \"stock\": \"4\"}}"}}
MacbookPro-2:src jchauvet$
```

### On AWS

We assume Serverless is setup and AWS named profiles are set too.
Please run command `cd src/ && make publish` to deploy lambda to AWS :

```bash
MacbookPro-2:src jchauvet$ make publish
Serverless: Packaging service...
#1 [internal] load build definition from Dockerfile
#1 sha256:b7c4376f97df0e7f8aab175712adb3ef32c53ba25caae42b2cb9e249d48426d0
#1 transferring dockerfile: 315B done
#1 DONE 0.0s

#2 [internal] load .dockerignore
#2 sha256:fcfd67b76db673d56a5e05b598a26ec70c2f9e1e304697a23e9c5b1e3cc12834
#2 transferring context: 2B done
#2 DONE 0.0s

#3 [internal] load metadata for public.ecr.aws/lambda/python:3.8
#3 sha256:6bbcd3f941ae4404b56ba294eee904a86c000166afdef9600cc56b41d32c2fdb
#3 DONE 0.5s

#5 [internal] load build context
#5 sha256:2a168e2b027d3598a1004b8a969cf29b5616e74b5f91335adf9d5354a456c8a9
#5 transferring context: 726B done
#5 DONE 0.0s

#4 [1/4] FROM public.ecr.aws/lambda/python:3.8@sha256:1058f198813cd449f2d3283cdf1d1afceb6a21a2a047a1eb1c65ef0e63e676de
#4 sha256:4e9f82aa00d96114def6914d6663b3ecbd06c2b940b151928c6c5404b1991109
#4 CACHED

#6 [2/4] COPY app.py /var/task
#6 sha256:7a66dcca4b18bed9789462dd73d6e04d0f664cabbd359fbc5a7aa33a6b081687
#6 DONE 0.0s

#7 [3/4] COPY requirements.txt /var/task
#7 sha256:3dc967149ec0e74861eccb4a84c06ddec59fe6a5456dfbfa1db6c593d056b15e
#7 DONE 0.0s

#8 [4/4] RUN python3 -m pip install -r requirements.txt
#8 sha256:adf71d8850b6470f58166c22b2816fdf794a7699e32981c3dba3652729fa31a2
#8 0.867 Collecting aws-xray-sdk
#8 0.988   Downloading aws_xray_sdk-2.8.0-py2.py3-none-any.whl (98 kB)
#8 1.231 Collecting faker
#8 1.277   Downloading Faker-8.9.1-py3-none-any.whl (1.2 MB)
#8 2.595 Collecting botocore>=1.11.3
#8 2.617   Downloading botocore-1.20.105-py2.py3-none-any.whl (7.7 MB)
#8 3.174 Collecting future
#8 3.199   Downloading future-0.18.2.tar.gz (829 kB)
#8 3.764 Collecting wrapt
#8 3.789   Downloading wrapt-1.12.1.tar.gz (27 kB)
#8 4.119 Collecting python-dateutil<3.0.0,>=2.1
#8 4.143   Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
#8 4.204 Collecting jmespath<1.0.0,>=0.7.1
#8 4.229   Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
#8 4.324 Collecting urllib3<1.27,>=1.25.4
#8 4.348   Downloading urllib3-1.26.6-py2.py3-none-any.whl (138 kB)
#8 4.413 Collecting six>=1.5
#8 4.437   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
#8 4.511 Collecting text-unidecode==1.3
#8 4.534   Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
#8 4.557 Using legacy 'setup.py install' for future, since package 'wheel' is not installed.
#8 4.557 Using legacy 'setup.py install' for wrapt, since package 'wheel' is not installed.
#8 4.638 Installing collected packages: six, urllib3, python-dateutil, jmespath, wrapt, text-unidecode, future, botocore, faker, aws-xray-sdk
#8 4.831     Running setup.py install for wrapt: started
#8 5.118     Running setup.py install for wrapt: finished with status 'done'
#8 5.134     Running setup.py install for future: started
#8 5.831     Running setup.py install for future: finished with status 'done'
#8 7.601 WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
#8 7.601 Successfully installed aws-xray-sdk-2.8.0 botocore-1.20.105 faker-8.9.1 future-0.18.2 jmespath-0.10.0 python-dateutil-2.8.1 six-1.16.0 text-unidecode-1.3 urllib3-1.26.6 wrapt-1.12.1
#8 7.779 WARNING: You are using pip version 21.1.1; however, version 21.1.3 is available.
#8 7.779 You should consider upgrading via the '/var/lang/bin/python3 -m pip install --upgrade pip' command.
#8 DONE 8.1s

#9 exporting to image
#9 sha256:e8c613e07b0b7ff33893b694f7759a10d42e180f2b4dc349fb57dc6b71dcab00
#9 exporting layers
#9 exporting layers 0.8s done
#9 writing image sha256:329623c8ed8f7c75db2b1b32ad169a24a92fe674b22e3a2d0c249b332003b89f done
#9 naming to docker.io/library/serverless-myonlinebookstore-dev:myonlinebookstore_lambda_book done
#9 DONE 0.8s
Serverless: Login to Docker succeeded!
The push refers to repository [001122334455.dkr.ecr.us-east-1.amazonaws.com/serverless-myonlinebookstore-dev]
96e5162919ac: Preparing
d37205a9b77b: Preparing
36f55860bd2d: Preparing
c6ef48ecad19: Preparing
1119dec7f0d8: Preparing
d6fa53d6caa6: Preparing
f1882e92d61e: Preparing
01f532c5531e: Preparing
1b728d9a04ef: Preparing
d6fa53d6caa6: Waiting
f1882e92d61e: Waiting
01f532c5531e: Waiting
1b728d9a04ef: Waiting
d37205a9b77b: Pushed
36f55860bd2d: Pushed
f1882e92d61e: Pushed
c6ef48ecad19: Pushed
96e5162919ac: Pushed
d6fa53d6caa6: Pushed
01f532c5531e: Pushed
1119dec7f0d8: Pushed
1b728d9a04ef: Pushed
myonlinebookstore_lambda_book: digest: sha256:00772984527359e4a3ecf2a46d0572f04ed9248d341809228242b7d1377e12cd size: 2207
Serverless: WARNING: Function generate-book has timeout of 90 seconds, however, it's attached to API Gateway so it's automatically limited to 30 seconds.
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
CloudFormation - CREATE_IN_PROGRESS - AWS::CloudFormation::Stack - myonlinebookstore-dev
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_COMPLETE - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_COMPLETE - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_COMPLETE - AWS::CloudFormation::Stack - myonlinebookstore-dev
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
CloudFormation - UPDATE_IN_PROGRESS - AWS::CloudFormation::Stack - myonlinebookstore-dev
CloudFormation - CREATE_IN_PROGRESS - AWS::Logs::LogGroup - generate-bookLogGroup
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::Logs::LogGroup - generate-bookLogGroup
CloudFormation - CREATE_COMPLETE - AWS::Logs::LogGroup - generate-bookLogGroup
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_COMPLETE - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Function - generate-bookLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Function - generate-bookLambdaFunction
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Function - generate-bookLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - generate-bookLambdaVersionPlIpqSXBZobMLngZczahKKk6FNud90urtAsIuN98
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - generate-bookLambdaVersionPlIpqSXBZobMLngZczahKKk6FNud90urtAsIuN98
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - generate-bookLambdaPermissionApiGateway
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - generate-bookLambdaVersionPlIpqSXBZobMLngZczahKKk6FNud90urtAsIuN98
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - generate-bookLambdaPermissionApiGateway
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Permission - generate-bookLambdaPermissionApiGateway
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodGet
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Method - ApiGatewayMethodGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1625430344277
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1625430344277
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1625430344277
CloudFormation - UPDATE_COMPLETE_CLEANUP_IN_PROGRESS - AWS::CloudFormation::Stack - myonlinebookstore-dev
CloudFormation - UPDATE_COMPLETE - AWS::CloudFormation::Stack - myonlinebookstore-dev
Serverless: Stack update finished...
Service Information
service: myonlinebookstore
stage: dev
region: us-west-2
stack: myonlinebookstore-dev
resources: 10
api keys:
  None
endpoints:
  GET - https://xxyyzzaabb.execute-api.us-east-1.amazonaws.com/dev/
functions:
  generate-book: myonlinebookstore-dev-generate-book
layers:
  None

Stack Outputs
generate-bookLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:001122334455:function:myonlinebookstore-dev-generate-book:1
ServiceEndpoint: https://xxyyzzaabb.execute-api.us-east-1.amazonaws.com/dev/
ServerlessDeploymentBucketName: myonlinebookstore-dev-serverlessdeploymentbucket-randomserverlessstring

MacbookPro-2:src jchauvet$
```

When your Lambda is deploy, you can execute command `cd src/ && make-run-test-aws` :

```bash
MacbookPro-2:src jchauvet$ make run-test-query-aws
{
    "statusCode": 200,
    "body": {
        "body": "{\"book\": {\"isbn\": \"978-0-10-548818-7\", \"title\": \"Although employee operation least better close.\", \"author\": \"Peter Smith\", \"stock\": \"19\"}}"
    }
}
MacbookPro-2:src jchauvet$
```

## Roadmap

[] Parsing payload to generate number of books given in parameter.
[] Adding X-Ray.
