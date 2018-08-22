print("ahello world")

import boto3

# dynamodb = boto3.resource('dynamodb')

dynamodb = boto3.resource('dynamodb', 
    endpoint_url='http://0.0.0.0:4569',
    aws_access_key_id = 'AccessKey',
    aws_secret_access_key = 'SecertKey')

table = dynamodb.create_table(
    TableName = 'usersa',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
            
        }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

print("hello world")


