import boto3

def upload_to_s3(file_name, bucket, key):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket, key)
    print(f"Uploaded {file_name} to s3://{bucket}/{key}")