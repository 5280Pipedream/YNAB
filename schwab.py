import os
import csv

with open('schwab.csv', 'r') as file_data:
	csv_data = csv.reader(file_data)
	next(csv_data)	# skips over the first row of file

	with open('new_schwab.csv', 'w', newline = '') as new_file:
		YNAB = ['Account', 'Date', 'Payee', 'Outflow', 'Inflow']
		csv_writer = csv.writer(new_file)
		csv_writer.writerow(YNAB)
		
		for line in csv_data:
			csv_writer.writerow(line)