import csv
import pandas as pd
import math
# from dotenv import load_dotenv
import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


subscriptions = []
Price = 0 
i = 0
try:
    amount = float(input("Please enter your budget"))
except:
    print("amount needs to be a number")
    exit()
filename = input("Please enter the name of the csv file")
column_transaction_name = input("Please enter the column name for transaction")
column_amount_name = input("Please enter the column name for amount")
try:            
    csv_file_path = pd.read_csv("{}.csv".format(filename),index_col=False) # a relative filepath
except:
    print("File in not founded")
    exit()
try:
    saved_transaction_column = list(csv_file_path[column_transaction_name])
    error_check = list(csv_file_path[column_amount_name])
except:
    print("Not a correct column")
    exit()
while True:
    subscription = input("Please provide your monthly subscriptions or DONE if finished: ")
    if subscription == "DONE":
        break
    else: 
        subscriptions.append(subscription)

#user includes their data in the csv file
for item in saved_transaction_column:
    i = i + 1
    for subscription in subscriptions:
        if(item.find(subscription) != -1):
            Price=float(csv_file_path.iloc[i-1][column_amount_name]) + Price
            if(math.isnan(Price)):
                print("Column was not found with a price")
                exit()
            
if (Price > amount):
    print (Price)
    print("You are over your monthly subscription budget")
elif(Price==amount):
    print(Price)
    print("You are spending your exact budget")
else:
    print(Price)
    print("You are spending below your maximum budget")


# with open(csv_file_path, 'rt') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
        # for subscription in subscriptions:
        #     if subscription in row[2]:
        #         Price=float(row[3]) + Price
        #         print(row[2], row[3])
        #         print(Price)





# ask_user_email_option = input("Would you like an email copy?")
# if(ask_user_email_option == "YES"):
#     your_email = input("Please enter an email")
#     message = Mail(
#         from_email=my_email,
#         to_emails=your_email,
#         subject='Subscription',
#         html_content=html
#         )
#     try:
#         sg = SendGridAPIClient(key)
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception:
#         print(Exception)
