#!/usr/bin/env python3
import os
import shutil
import psutil
import socket

import emails

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80
 
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
 
def check_available_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500
 
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'
 
check_states = {
    check_cpu_usage(): "CPU usage is over 80%",
    check_disk_usage("/"): "Available disk space is less than 20%",
    check_available_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}

error = False
error_message = ""

for action, err_message in check_states.items():
    if not action: 
        error_message = err_message
        error = True

if error:
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Error - {}".format(error_message)
    body = "Please check your system and resolve the issue as soon as possible"

    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)