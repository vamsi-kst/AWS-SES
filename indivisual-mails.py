import boto3

ACCESS_KEY = 'AKIAXJ36AG2OBPLTDUM7'
SECRET_ACCESS_KEY = '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'
REGION = 'ap-south-1'

client = boto3.client(
    'ses',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name=REGION
)

sender = 'trainings@patchupskills.com'
subject = 'Welcome to AWS SES'
#bcc_address = 'vikramkumar.t@knowledgesprint.com'

with open('recepients.txt', 'r') as file:
    for line in file:
        recipient = line.strip()

        message = f'''
            <p>Hello {recipient},</p>
            <p>This is the first paragraph of the message.</p>
            <p>This is the second paragraph of the message.</p>
            <p>Regards,<br>Asif</p>
        '''

        response = client.send_email(
            Source=sender,
            Destination={
                'ToAddresses': [recipient],
                #'BccAddresses': [bcc_address]
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': message,
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': message,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        print(f"Email sent to {recipient}: {response['MessageId']}")
