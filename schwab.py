import os
import csv

data = []

with open('data.csv', 'r') as file_data:
	csv_data = csv.reader(file_data, delimiter = ',')
	#next(csv_data)	# skips over the first row of file
	#next(csv_data)index.

	# Finds the line where posted transactions start
	for line in csv_data:
		if line[0] == 'Posted Transactions':
			posted_line_number = csv_data.line_num
			print(posted_line_number)
	
	# able to find the line number that we want to start after. Now need to parse that data.
	# this line will be different each time so we need a function for it?

'''
This is the output file. Needs to read the data put together from above.

	with open('new_schwab.csv', 'w', newline = '') as new_file:
		YNAB = ['Account', 'Date', 'Payee', 'Outflow', 'Inflow']
		csv_writer = csv.writer(new_file)
		csv_writer.writerow(YNAB)
		
		for line in csv_data:
			csv_writer.writerow(line)
'''