import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

subject = "Email Subject"
body = "This is the body of the text message"
sender = "ipaddress.adamstown@gmail.com"
recipients = ["cullenhenry2016@gmail.com", "ipaddress.adamstown@gmail.com"]
password = "Gory5-Showcase9-Shamrock5-Machine6-Blazing4"


#get poassword from dotenv
password = os.getenv("PASSWORD")
device = os.getenv("DEVICE")
print(password, device)


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")

send_email(subject, body, sender, recipients, password)
