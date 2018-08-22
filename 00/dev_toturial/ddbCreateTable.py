print("ahello world")

import boto3

# dynamodb = boto3.resource('dynamodb')

dynamodb = boto3.resource('dynamodb', 
    endpoint_url='http://0.0.0.0:4569',
    aws_access_key_id = 'AccessKey',
    aws_secret_access_key = 'SecertKey')

table = dynamodb.create_table(
    TableName = 'aws_flashcard',
    KeySchema=[
        {
            'AttributeName': 'question',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'answer',
            'KeyType': 'RANGE'
            
        }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'question',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'answer',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

table.meta.client.get_waiter('table_exists').wait(TableName='aws_flashcard')
print(table.item_count)

print("hello world")


