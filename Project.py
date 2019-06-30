import csv
import pandas as pd
from dotenv import load_dotenv
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

subscriptions = []
while True:
    subscription = input("Please provide your monthly subscriptions or DONE if finished: ")
    if subscription == "DONE":
        break
    else: 
        subscriptions.append(subscription)


#user includes their data in the csv file

            
csv_file_path = "bank_accounts.csv" # a relative filepath

with open(csv_file_path, 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for subscription in subscriptions:
            if subscription in row[2]:
                print(row[2], row[3])