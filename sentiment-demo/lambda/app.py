import os
import json
import boto3

def handler(event, context):
    client = boto3.client('comprehend')
    
    body = json.loads(event["body"])  # Assuming event["body"] is a JSON string
    text = body.get("text", "")       # Extract the 'text' field safely

    sentiment = client.detect_sentiment(Text=text, LanguageCode='en')

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "sentiment": sentiment
        })
    }

