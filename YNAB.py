# format to YNAB csv format (headers) for import into YNAB

import os
import pandas as pd 
import datetime

location = r'D:\dev\YNAB\schwab.csv'
schwab = pd.read_csv(location)
Account = 'Investor Checking'
YNAB = ['Account', 'Date', 'Payee', 'Outflow', 'Inflow']
