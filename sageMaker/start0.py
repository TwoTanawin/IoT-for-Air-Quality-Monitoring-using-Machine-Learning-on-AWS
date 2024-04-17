import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('sagemaker')

    #wish to get current status of instance
    status = client.describe_notebook_instance(NotebookInstanceName='sagemaker-schedule')
    
    #Start the instance
    
    client.start_notebook_instance(NotebookInstanceName='sagemaker-schedule')
    
    
    # client = boto3.client('sagemaker')
    # client.start_notebook_instance(NotebookInstanceName='schedule-notebook')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }