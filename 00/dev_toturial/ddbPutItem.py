print("ahello world")

import boto3

# dynamodb = boto3.resource('dynamodb')

dynamodb = boto3.resource('dynamodb', 
    endpoint_url='http://0.0.0.0:4569',
    aws_access_key_id = 'AccessKey',
    aws_secret_access_key = 'SecertKey')

table = dynamodb.Table('aws_flashcard')
table.put_item(
    Item={
        'question': 'What is cmd to disable root access? ',
        'answer': 'sudo passwd -l root.',
        'tag': 'ec2'
    })


print(table.item_count)

print("hello world")


