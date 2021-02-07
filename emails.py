#!/usr/bin/env python3

'''
This is the script that prepares email messages. The functions are called by other scripts.
generate_email is for emailng reports
generae_error_email is for emailing monitoring alerts
'''

from email.message import EmailMessage
import os.path
import smtplib
import mimetypes

def generate_email(From, To, subject, body, attachment):
    message = EmailMessage()
    sender = From
    recipient = To
    message["From"] = From
    message["To"] = To
    message["Subject"] = subject
    message.set_content(body)
    attachment_path = attachment
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/',1)
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = os.path.basename(attachment_path))
    return message

def generate_error_email(From, To, subject, body):
    message = EmailMessage()
    sender = From
    recipient = To
    message["From"] = From
    message["To"] = To
    message["Subject"] = subject
    message.set_content(body)
    return message

def send_email(login, password, message):
    mail_server = smtplib.SMTP('localhost')
    mail_pass = password
#    mail_server.login(login, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
