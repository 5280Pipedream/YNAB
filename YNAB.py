#!/usr/bin/env python3
# format to YNAB csv format (headers) for import into YNAB

import os
import pandas as pd 
import datetime
import csv
'''
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
'''
# everything above this may now be junk given solution below

'''
TO DO:
	Add a column for account type, though that may be unessary
	new_data is clean and ready to be put into a new CSV file
	Add necessary header to new CSV file - test if header is necessary
	Test import of new CSV file into YNAB
	Add process for capital one
	Add procedure to automatically find csv files in downloads folder
'''

account = ''
date = []
Payee = []
Outflow = []
Inflow = []
pt = []

with open('schwab.csv', 'r') as file:
	reader = csv.reader(file)
	data = [r for r in reader]

# grabs all the data up to Posted transactions and puts them in a list
for line in data:
	if line[0] == 'Posted Transactions':
		break
	pt.append(f"{line[0]}")

'''
counts the list created in pt and adds one so that we can delete all
the data above Posted Transactions
'''
pt_position = len(pt) + 1

# generates a new data set
new_data = [r for r in data]

# deletes all data before Posted Transactions
del new_data[:pt_position]

# removes type, check number, running balance
for row in new_data:
	del row[1:3]
	del row[-1]

# tests output
for row in new_data:
	print(row)