import boto3

s3 =boto3.resource("s3")

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':region})
    print("create bucket susscesfully")

def upload_buckup(s3,file_name,bucket_name,key_name):
    data=open(file_name,'rb')    # read in binary
    s3.Bucket(bucket_name).put_object(Key=key_name,Body=data)
    print("backup uploaded succesfully")

bucket_name="python-for-devops-by-rakesh-012334"
region='us-east-2'

#create_bucket(s3,bucket_name,region)
file_name=r"\Users\Charan\Desktop\python\chapter 4\backup\backups2026-01-04.tar.gz.tar.gz"
upload_buckup(s3,file_name,bucket_name,"my-backup.tar.gz")