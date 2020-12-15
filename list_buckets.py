import boto3
import os

s3 = boto3.resource('s3')

boto3_session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=os.environ['AWS_REGION'])

for bucket in s3.buckets.all():
    print(bucket.name)
