import boto3
import json

def lambda_handler(event, context):
    
    client = boto3.client('dynamodb')
    
    response = client.put_item(
        TableName='esp32Data3',
        Item={
            'time': {'S': event['time']},
            'random_value': {'N': str(event['random_value'])}
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
