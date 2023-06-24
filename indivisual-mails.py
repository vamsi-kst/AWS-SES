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
sender_name = 'Patchup Skills Online Training Team'
subject = 'FREE Demo On Salesforce by Mrs. Komal On 26th June 2023 @ 8:00 AM (IST)'
#bcc_address = 'vikramkumar.t@knowledgesprint.com'

with open('recepients.txt', 'r') as file:
    for line in file:
        recipient = line.strip()

        message = f'''
            <p>Hi,</p>
            <p>Greetings from <strong>Patchup Skills Technologies !</strong></p>
            <p></p>
            <p>We are happy to inform you that our New Special offer Batch of Salesforce Online Training Program Starts on <strong><span style="color: green;">26th July 2023 @ 8:00 AM (IST)</span> by RealTime Expert, <span style="color: green;">Mrs. Komal</span></strong></p>
            <p></p>
            <p><strong><span style="font-size: 18px;">Details of the course are as stated below:</strong></p>
            <ul>
                <li>Demo link: <a href="https://meet.goto.com/367127477">https://meet.goto.com/367127477</a></li>
                <li>Duration: <strong>2 Months</li>
                <li>Offer Fee: <span style="color: green;">
                <strong>Rs.15,000/- (With Videos).<br>
                <span style="padding-left: 62px;">Rs.10,000/- (Without Videos).</strong></span></li>
                <p></p>
                <li>Course Content Link: <a href="https://shorturl.at/fBGKX">https://shorturl.at/fBGKX</a></li>
            </ul>
            <p><strong><span style="font-size: 24px;">Register Now! Limited Seats Available!</strong></p>
            <p>For New Batches Visit: <a href="https://patchupskills.com/online-training/">https://patchupskills.com/online-training/</a></p>
            <p>Share this information and encourage your friends to attend the free online demo session.</p>
            <p>Any changes/updates will be communicated via email.</p>
            <p>Please email your online-related queries to trainings@patchupskills.com, or call/Whatsapp us on +91-9121784514.</p>
            <p><span style="font-size: 18px;">Patchup Skills Technologies wishes you a Good Day!</p>
            <p>Regards,<br>Online Training Team<br>Patchup Skills Technologies<br>Mobile: +91-9121784514<br><a href="https://patchupskills.com">https://patchupskills.com</a></p>
        '''

        response = client.send_email(
            Source=f'{sender_name} <{sender}>',
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
            },

        )

print(f"Email sent to {recipient}: {response['MessageId']}")
