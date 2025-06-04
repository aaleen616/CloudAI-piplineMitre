import boto3

def lambda_handler(event, context):
    print("Alert Triggered:", event)
    # Add SNS or notification logic here