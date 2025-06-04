import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        print("Ingested file content:", content)
        # Add validation/transformation logic here