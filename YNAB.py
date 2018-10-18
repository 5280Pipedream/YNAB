#!/usr/bin/env python3
# format to YNAB csv format (headers) for import into YNAB

import os
import datetime
import csv

"""
TO DO:
	Add process for chase bank files
	Error checking
	duplicate files found in directory

"""
ynab_headers = ["Date", "Payee", "Outflow", "Inflow"]
# place holder for schwab. Holds all rows for garbage data to be deleted
pt = []
# directory where csv files are saved. Change to proper directory if different
path = "D:\Downloads"

# gets csv files from downloads directory
schwab_file = [
    i
    for i in os.listdir(path)
    if os.path.isfile(os.path.join(path, i)) and "XXXXXX" in i
]
chase_file = [
    i
    for i in os.listdir(path)
    if os.path.isfile(os.path.join(path, i)) and "Chase" in i
]
captial_one_file = [
    i
    for i in os.listdir(path)
    if os.path.isfile(os.path.join(path, i)) and "transaction_download" in i
]

# converts the file names from list to string
schwab_f = "".join(schwab_file)
chase_f = "".join(chase_file)
captial_f = "".join(captial_one_file)

# changes to the download directory
os.chdir(path)

# check if file exists
if schwab_f == "":
    print("Schwab file not found")
else:
    # opens the schwab csv file and reads it to the data variable
    with open(schwab_f, "r") as file:
        reader = csv.reader(file)
        data_s = [r for r in reader]

        # grabs all the data up to Posted transactions and puts them in a list
    for line in data_s:
        if line[0] == "Posted Transactions":
            break
        pt.append(f"{line[0]}")

        # counts the list created in pt and adds one so that we can delete all
        # the data above Posted Transactions
    pt_position = len(pt) + 1

    # deletes all data before Posted Transactions
    del data_s[:pt_position]

    # removes type, check number, running balance
    for row in data_s:
        del row[1:3]
        del row[-1]

        # writes data to new csv for import into ynab
    with open("schwab_ready_for_import.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(ynab_headers)
        for row in data_s:
            writer.writerow(row)
    print("Schwab import file created")

# check if file exists
if captial_f == "":
    print("Capital One file not found")
else:
    # opens captial one csv for reading
    with open(captial_f, "r") as file:
        reader = csv.reader(file)
        data_c = [r for r in reader]

        # deletes header
    del data_c[0]

    # deletes transaction status and date and category
    for row in data_c:
        del row[0:2]
        del row[-3]

        # deletes last 4 digits of account
    for row in data_c:
        del row[1]

        # writes clean data to new csv file for import
    with open("capitalone_ready_for_import.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(ynab_headers)
        for row in data_c:
            writer.writerow(row)
    print("Capital One import file created")
