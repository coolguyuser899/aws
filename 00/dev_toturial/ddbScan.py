print("ahello world")

import boto3
from time import sleep

dynamodb = boto3.resource('dynamodb', 
    endpoint_url='http://0.0.0.0:4569',
    aws_access_key_id = 'AccessKey',
    aws_secret_access_key = 'SecertKey')

table = dynamodb.Table('aws_flashcard')
response = table.scan()
data = response['Items']
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])
    
print(data)
    
print("hello world")
