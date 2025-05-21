import boto3
import json


ses = boto3.client('ses')


def lambda_handler(event, context):
    try:
        # Validate input
        required_fields = ['email', 'subject', 'message']
        if not all(field in event for field in required_fields):
            raise ValueError("Missing required fields")
            
        response = ses.send_email(
            Source='verified-email@example.com',  # Replace with your SES email
            Destination={'ToAddresses': [event['email']]},
            Message={
                'Subject': {'Data': event['subject']},
                'Body': {'Text': {'Data': event['message']}}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully', 'response': response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
