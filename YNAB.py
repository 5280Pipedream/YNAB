# format to YNAB csv format (headers) for import into YNAB

import os
import csv
import pandas as pd


# TODO:
# 	Add process for chase bank, care credit and other financial institutions
# 	Error checking
# 	duplicate files found in directory
#     date checking & formatting
#         Capital one changed format (OCT 2019) broke YNAB import
#         YNAB = 'MM/DD/YYYY'
#         Capital one = 'YYYY-MM-DD'
#     Use pandas for all CSV files


ynab_headers = ["Date", "Payee", "Outflow", "Inflow"]
# place holder for schwab. Holds all rows for garbage data to be deleted
pt = []
# temp fix for different user profiles on pcs
computer = os.getenv("COMPUTERNAME")
# directory where csv files are saved. Change to proper directory if different
if computer == "SUPPORT-7510":
    path = "D:\Downloads"
else:
    path = os.getenv("USERPROFILE") + "\downloads"

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
capital_one_file = [
    i
    for i in os.listdir(path)
    if os.path.isfile(os.path.join(path, i)) and "transaction_download" in i
]

# converts the file names from list to string
schwab_f = "".join(schwab_file)
chase_f = "".join(chase_file)
capital_f = "".join(capital_one_file)

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
if capital_f == "":
    print("Capital One file not found")
else:
    # converts capital one file
    df = pd.read_csv(capital_f)
    df.drop(["Transaction Date", "Card No.", "Category"], axis=1, inplace=True)
    df["Posted Date"] = pd.to_datetime(df["Posted Date"])
    df["Posted Date"] = df["Posted Date"].dt.strftime("%m/%d/%Y")
    df.to_csv("capitalone_ready_for_import.csv", header=ynab_headers, index=False)
    print("CREATED capitalone_ready_for_import.csv")

exit()
