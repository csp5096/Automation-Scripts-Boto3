#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-25cf1c5d',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print (instance[0].id)
