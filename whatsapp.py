from twilio.rest import Client


account_sid = 'your_account_sid'  
auth_token = 'your_auth_token'    
twilio_number = 'whatsapp:+14155238886'  
recipient_numbers = [
    'whatsapp:+12345678901',  
  
]

message_body = "Hello from Python! This is an automated WhatsApp message."


client = Client(account_sid, auth_token)


def send_whatsapp_messages():
    for number in recipient_numbers:
        try:
           
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,  
                to=number            
            )
            print(f"Message sent to {number}: {message.sid}")
        except Exception as e:
            print(f"Failed to send message to {number}: {str(e)}")

send_whatsapp_messages()
