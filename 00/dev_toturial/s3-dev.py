import boto3

# list bucket
s3 = boto3.client('s3', endpoint_url='http://0.0.0.0:4572/',
        aws_access_key_id = 'AccessKey',
        aws_secret_access_key = 'SecertKey')
        
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)

# create bucket
s3.create_bucket(Bucket='my-bucket')
 
# upload a file
bucket_name = 'my-bucket'
s3.upload_file('/tmp/hello.txt', 'my-bucket', 'hello.txt')


