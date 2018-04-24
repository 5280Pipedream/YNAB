#!/usr/bin/env python3
# format to YNAB csv format (headers) for import into YNAB

import os
import pandas as pd 
import datetime
import csv

'''
TO DO:
	Add a column for account type, though that may be unessary
	Test import of new CSV file into YNAB
	Add process for capital one and chase files
'''
ynab_headers = ['Date', 'Payee', 'Outflow', 'Inflow']
pt = []

path = 'D:\Downloads'

# gets csv files from downloads directory
schwab_file = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and \
         'XXXXXX' in i]
chase_file = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and \
         'Chase' in i]
captial_one_file = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and \
         'transaction_download' in i]

# converts the file names from list to string
schwab_f = ''.join(schwab_file)
chase_f = ''.join(chase_file)
captial_f = ''.join(captial_one_file)

# test for files
# print(f"{schwab_f} * {chase_f} * {captial_f}")

# changes to the download directory
os.chdir(path)

# opens the schwab csv file and reads it to the data variable
with open(schwab_f, 'r') as file:
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

# writes data to new csv for import into ynab
with open('schwab_ready_for_import.csv', 'w', newline='') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(ynab_headers)
	for row in new_data:
		writer.writerow(row)