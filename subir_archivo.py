
import boto3
import json
import base64

s3 = boto3.client('s3')

def upload_file(event, context):
    bucket_name = event['queryStringParameters']['bucket']
    file_name = event['queryStringParameters']['file_name']
    base64_str = event['body']
    
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=base64.b64decode(base64_str))
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'File {file_name} uploaded to bucket {bucket_name}.')
    }
