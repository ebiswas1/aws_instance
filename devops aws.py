#devops 1

import time
import boto3
from boto3 import ec2
from botocore import exceptions 
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

def specs():
    ''' get input from user on specs of instance '''
    ImageID=input("image: ")
    InstanceType=input("instance type: ")
    KeyName=input("key name: ")
    return ImageID,InstanceType,KeyName

def create(ImageID,InstanceType,KeyName):
    ''' creating instance '''
    try:
        instance = ec2.create_instances(ImageId=ImageID, MinCount=1, MaxCount=1, InstanceType=InstanceType, KeyName=KeyName)
    except ClientError as err:
        err.error("Couldn't create instance. Here's why: %s: %s", err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    '''
    test ex. 
    instance = ec2.create_instances(ImageId="ami-0dafa01c8100180f8", MinCount=1, MaxCount=1, InstanceType="t2.micro", KeyName="111")
    '''

def destroy():
    if instance is None:
            print("No instance to terminate.")
            return
    try:
        instance.terminate()
        instance.wait_until_terminated()
        instance = None
    except ClientError as err:
            err.error("Couldn't terminate instance. Here's why: %s: %s", err.response['Error']['Code'], err.response['Error']['Message'])
            raise

def main():
    """
    main 
    """
    input = specs()
    create(input[0],input[1],input[2])
    time.sleep(90)
    destroy()
    print()

if __name__ == '__main__':
    main()