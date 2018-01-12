#!/usr/bin/env python

import sys
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})

for bucket_name in sys.argv[1:]:
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        print (response)
    except Exception as error:
        print (error)

