import boto3

client = boto3.client('s3')
response = client.create_bucket(
    #ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
    Bucket='boto3-test-bucket-uday',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1' # without mentioning the region, the program is not working as in the video
    },
    
)