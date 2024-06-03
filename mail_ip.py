import smtplib
import os
import requests
import json
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def main():
    password = os.getenv("PASSWORD")
    device = os.getenv("DEVICE")
    sender = os.getenv("EMAIL")
    subject = "IP Address of the " + device
    public_ip = get_public_ip()
    body = "Hi there "+ sender +",\n\nThe public IP address of the " + device + " is " + public_ip + ".\nThx for using the service. \n\nRegards, \nYour friendly bot"
    # Usefull for debugging
    # print(password, device, sender, subject, body)
    send_email(subject, body, sender, password)


def send_email(subject, body, sender, password):
    print("Sending email...")
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = sender

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, sender, msg.as_string())
        print("Message sent!")

def get_public_ip():
    print("Getting public IP from https://ipinfo.io/json...")
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify=True)
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    data = response.json()
    print("Public IP: ", data['ip'])
    return data['ip']

if __name__ == '__main__':
    main()
