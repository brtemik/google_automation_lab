#!/usr/bin/env python3

'''
This is a simple monitoring script. It aletrs administrator via email if one of further things happen:
1) If CPU usage is above 80%
2) If there is less than 500MB of RAM available
3) If there is less than 20% of Disk space left
4) If server can't resolve localhost
'''

import psutil
import socket
import emails

cpu = psutil.cpu_percent(interval = 1)
v_memory = psutil.virtual_memory().available
disk = psutil.disk_usage('/').percent #used
def hostname_resolver(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False
From = 'automation@example.com'
To = 'student-00-b0c51666e7f0@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'
if cpu > 80.0:
    subject = 'Error - CPU usage is over 80%'
    message = emails.generate_error_email(From, To, subject, body)
    emails.send_email('student-00-b0c51666e7f0', '35MrNSxdzH5', message)
if v_memory < (500*1024*1024):
    subject = 'Error - Available memory is less than 500MB'
    message = emails.generate_error_email(From, To, subject, body)
    emails.send_email('student-00-b0c51666e7f0', '35MrNSxdzH5', message)
if disk > 80.0:
    subject = 'Error - Available disk space is less than 20%'
    message = emails.generate_error_email(From, To, subject, body)
    emails.send_email('student-00-b0c51666e7f0', '35MrNSxdzH5', message)
if not hostname_resolver('localhost'):
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    message = emails.generate_error_email(From, To, subject, body)
    emails.send_email('student-00-b0c51666e7f0', '35MrNSxdzH5', message)

