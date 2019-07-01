import csv
import pandas as pd
import math
from dotenv import load_dotenv
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

subscriptions = []
response = ""
Price = 0 
i = 0
load_dotenv()
key = os.environ.get("API")
my_email = os.environ.get("email")
try:
    amount = float(input("Please enter your budget: "))
except:
    print("amount needs to be a number")
    exit()
filename = "bank_accounts"
column_transaction_name = "Description"
column_amount_name = "Debit"
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

Price_usd = to_usd(Price)
amount_usd = to_usd(amount)
if (Price > amount):
    print(f"You spent {Price_usd} on subscriptions but only budgeted {amount_usd}. Cancel a subscription")
    response =f"You spent {Price_usd} on subscriptions but only budgeted {amount_usd}. Cancel a subscription"   
elif(Price==amount):
    print("You are spending your exact budget")
    response = "You are spending your exact budget"
else:
    print(f"You spent {Price_usd} on subscriptions, which is below your budget of  {amount_usd}. Good job!")
    response = f"You spent {Price_usd} on subscriptions, which is below your budget of  {amount_usd}. Good job!"

html = """<html>
<body>
<h1>Thank you for using our service<h1>
<p>The subscriptions {subscriptions}<p/>
<p>The price you did not want to go over: {amount}</p>
<p>What we found from the csv: {response} </p>
</body>
</html>""".format(subscriptions = str(subscriptions),amount = amount, response = response)

ask_user_email_option = input("Would you like an email copy?")
if(ask_user_email_option == "YES"):
    your_email = input("Please enter an email")
    message = Mail(
        from_email=my_email,
        to_emails=your_email,
        subject='Subscription',
        html_content=html
        )
    try:
        sg = SendGridAPIClient(key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception:
        print(Exception)




