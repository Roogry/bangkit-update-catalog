#!/usr/bin/env python3
import os 
from datetime import date

import reports
import emails

fruit_data = []
desc_path = 'supplier-data/descriptions/'

def process_data(fruit_data):
    formated_data = []
    for fruit in fruit_data:
        formated_data.append("name: {}<br/>weight: {}\n".format(fruit[0], fruit[1]))
    return formated_data

for text_file in os.listdir(desc_path):
    with open(desc_path + text_file, 'r') as opened:
        fruit_data.append([line.strip() for line in opened.readlines()])
 
if __name__ == "__main__":
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    formated_data = process_data(fruit_data)
    body = "<br/><br/>".join(formated_data)
    report_file_path = "/tmp/processed.pdf"
    reports.generate_report(report_file_path, title, body)

    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate_email(sender, recipient, subject, body, report_file_path)
    emails.send_email(message)