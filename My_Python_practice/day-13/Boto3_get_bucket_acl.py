import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='uk-s3-bucket',
    
)
print(response["Owner"]["ID"])