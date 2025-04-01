import boto3

# Specify the correct region
client = boto3.client('s3', region_name='ap-south-1')

response = client.create_bucket(
    Bucket='sona-boto3-demo-bucket',  
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket Created Successfully:", response)
