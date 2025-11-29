
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_email = 'your_email@gmail.com'  
sender_password = 'your_email_password'  
smtp_server = 'smtp.gmail.com'
smtp_port = 587


recipient_emails = [
    'recipient1@example.com',
    
]


subject = "Hello from Python!"
body = "This is an automated email sent from a Python script. Hope you're doing well!"

def send_email():
    try:
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
       
        server.login(sender_email, sender_password)
        print("Logged in successfully!")
        
        for recipient in recipient_emails:
           
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

          
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")
        
        
        server.quit()

    except Exception as e:
        print(f"Error: {e}")


send_email()


