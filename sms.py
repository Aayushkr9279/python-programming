from twilio.rest import Client
import time

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'

client = Client(account_sid, auth_token)

phone_numbers = [
    '+12345678901',
]

message_body = "Hello! This is an automated SMS sent by a Python script."

def send_sms():
    for number in phone_numbers:
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=number
            )
            print(f"Message sent to {number}: {message.sid}")
            time.sleep(1)
        except Exception as e:
            print(f"Failed to send message to {number}: {str(e)}")

send_sms()
