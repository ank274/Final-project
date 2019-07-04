# Final-project
Before using the python program, from within a virtual environment, install the following packages using pip install:

pandas; 
dotenv;
pytest (for developers / those who'd like to test the definition function)
******************************************
Follow the following steps only if you'd like an email copy of your results at the end:

Install 

sendgrid==6.0.5 

in your virtual environment using pip install.

Then go to sendgrid.com and obtain an API key. Create a '.env' file and include your API key as: 
API = "Input your API". 
my_email = "your email"

Lastly, within the .gitignore file, type .env (this should already be done for you)
*************************************************
Reminder- Put the CSV in the same folder as the Python file
Next, load your bank statement(s) into the bank_accounts.csv file that has been setup. Please ensure that the description of the transaction  and the value of the transaction are under columns 'Description' and 'Debit', respectively. 

Next, run the program (python Project.py) through your command line, within the virtual environment. 

Now follow the instructions of the program to determine how much you'd like to be spending on monthly subscriptions and how much you're actually spending. Have fun!
