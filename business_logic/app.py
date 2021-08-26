import os
import boto3
import json

from boto3.dynamodb.types import TypeDeserializer

def lambda_handler(event, context):
    """
    Receives a message from the Queue, applies some business logic, and then 
    updates the record in the dynamo table
    """

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ['TABLE'])

    for record in event['Records']:
	body = json.loads(record['body'])

	## Business logic to edit the item


        Table.put(
	    Item = body
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
        }),
    }