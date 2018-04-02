#!/usr/bin/env python3
# format to YNAB csv format (headers) for import into YNAB

import os
import pandas as pd 
import datetime

location = r'E:\Projects\YNAB\schwab.csv'
schwab = pd.read_csv(location)
YNAB = ['Account', 'Date', 'Payee', 'Outflow', 'Inflow']

schwab = pd.read_csv(location, names = ['Date', 'Type', 'Check #', 'Payee', 'Outflow', 'Inflow', 'Running Balance'])
 # remove columns
del schwab['Type']
del schwab['Check #']
del schwab['Running Balance']
# add account column
schwab['Account'] = 'Investor Checking'
# order columns to match YNAB
schwab[['Account', 'Date', 'Payee', 'Outflow', 'Inflow']] # sort by columns
# export to CSV
schwab.to_csv(r'E:\Projects\YNAB\schwab_ReadyToExport.csv')
