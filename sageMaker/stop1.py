import json
import boto3
import time

def lambda_handler(event, context):
    client = boto3.client('sagemaker')

    # Start the instance
    client.start_notebook_instance(NotebookInstanceName='sagemaker-schedule')

    # Wait for 10 minutes
    time.sleep(600)

    # Stop the instance after 10 minutes
    client.stop_notebook_instance(NotebookInstanceName='sagemaker-schedule')

    return {
        'statusCode': 200,
        'body': json.dumps('Instance stopped after 10 minutes!')
    }
