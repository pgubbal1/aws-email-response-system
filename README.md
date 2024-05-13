# Automated Customer Inquiry Response System

## Overview
This system automates responses to customer inquiries using AWS Simple Email Service (SES) and AWS Lambda. It is designed to quickly acknowledge customer emails sent to support@quickhelpservice.com.

## System Architecture
- **AWS SES**: Receives emails and triggers a Lambda function.
- **AWS Lambda**: Processes incoming emails and sends a predefined response.

## Setup and Deployment
### Verify Email Address
Ensure that support@quickhelpservice.com is verified in AWS SES.

### Deploy Lambda Function
1. Create a new Lambda function in the AWS Management Console.
2. Copy and paste the code from `lambda_function.py` into the function's code editor.
3. Set the function's execution role to one that has permissions for SES operations and CloudWatch logging.

## Usage
Send an email to support@quickhelpservice.com to trigger the system. The function will log the receipt and send back a confirmation email.
