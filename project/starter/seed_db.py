import boto3
import uuid

table = boto3.resource('dynamodb', region_name='us-east-1').Table('BugReports-9e3628b0')

item = {
    'ticketId': 'BUG-' + str(uuid.uuid4())[:8],
    'description': 'Checkout page freezes on pay button',
    'stepsToReproduce': '1. Add items to cart 2. Click checkout 3. Click pay',
    'environment': 'Chrome on macOS'
}

table.put_item(Item=item)
print(f"Successfully created ticket {item['ticketId']} in DynamoDB!")