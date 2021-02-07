#!/usr/bin/env python3

'''
This is like 'main' script for handling email stuff. It calls functions from other scripts
to generate and send email with pdf reports.
'''

import os
import datetime
import reports
import emails


text = ''
descriprions = os.listdir('/home/student-00-b0c51666e7f0/supplier-data/descriptions/')
for desc in descriprions:
    path = '/home/student-00-b0c51666e7f0/supplier-data/descriptions/' + desc
    with open(path, 'r') as file:
        content = file.readlines()
        text += 'name: ' + content[0] +'<br/>' + 'weight: ' + content[1] + '<br/>' + '<br/>'

if __name__ == "__main__":
    title = 'Processed Update on ' + datetime.date.today().strftime("%B %d, %Y")
    paragraph = text
    reports.generate_report('/tmp/processed.pdf', title, paragraph)
    From = 'automation@example.com'
    To = 'student-00-b0c51666e7f0@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully.\nA detailed list is attached to this email.'
    attachment = '/tmp/processed.pdf'
    message = emails.generate_email(From, To, subject, body, attachment)
    emails.send_email('student-00-b0c51666e7f0', '35MrNSxdzH5', message) #I know that keep credentials open is insecure, but in this lab its okay.
