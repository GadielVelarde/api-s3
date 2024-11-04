

import boto3
import json

s3 = boto3.client('s3')

def create_directory(event, context):
    bucket_name = event['queryStringParameters']['bucket']
    directory_name = event['queryStringParameters']['directory'] + '/'
    s3.put_object(Bucket=bucket_name, Key=directory_name)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Directory {directory_name} created successfully in bucket {bucket_name}.')
    }
