

import boto3
import json

s3 = boto3.client('s3')

def create_bucket(event, context):
    bucket_name = event['queryStringParameters']['bucket_name']
    s3.create_bucket(Bucket=bucket_name)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Bucket {bucket_name} created successfully.')
    }
