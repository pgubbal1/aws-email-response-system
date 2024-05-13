import boto3
import json

def lambda_handler(event, context):
    # Extract the SES message details
    ses_notification = event['Records'][0]['ses']
    mail = ses_notification['mail']
    sender = mail['source']
    subject = mail['commonHeaders']['subject']

    # Setup SES client
    ses_client = boto3.client('ses', region_name='us-east-1')  # Ensure the region matches your SES setup

    # Prepare the response email
    response_subject = "Re: " + subject
    response_body = """
    Hello,

    Thank you for your inquiry. We have received your message and will get back to you within 24 hours.

    Best regards,
    The Quick Help Service Team
    """
    response_email = {
        "Source": 'support@quickhelpservice.com',  # Your verified sender email address
        "Destination": {
            "ToAddresses": [
                sender  # Send the response back to the original sender
            ]
        },
        "Message": {
            "Subject": {
                "Data": response_subject
            },
            "Body": {
                "Text": {
                    "Data": response_body
                }
            }
        }
    }

    # Send the email
    try:
        response = ses_client.send_email(**response_email)
        print("Response email sent successfully to:", sender)
    except Exception as e:
        print("Error sending response email:", e)

    return {
        'statusCode': 200,
        'body': json.dumps('Email processed and response sent successfully')
    }
