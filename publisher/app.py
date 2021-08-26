import os
import boto3
import json

from boto3.dynamodb.types import TypeDeserializer

def lambda_handler(event, context):
    """
    Takes a message from the DynamoDB stream, serializes it, and publishes the 
    message to the Topic for broadcast
    """

    sns = boto3.resource("sns")
    topic = sns.Topic(os.environ['TOPIC'])
    deserializer = TypeDesiralizer()

    for record in event['Records']:
        event_name = record['eventName']
        raw_item = event_name['dynamodb']['NewImage']
        item = {k: desializer.deserialize(v) for k, v in raw_items()}
        topic.publish(
            Message=json.dumps(item)
        )
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Sucess",
        }),
    }
