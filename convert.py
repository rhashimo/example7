#!/usr/bin/env python3

import csv
from datetime import datetime
from pprint import pprint

# 1. load input.csv into a variable called `polls`
with open("input.csv") as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows]

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open("output.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerow(["data", "approve"])

	# 3. Loop through each row of `polls` 
	for row in rows:
	    # 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
		raw_date = row["enddate"]
		approve = row["approve"]

		date = datetime.strptime(raw_date, "%m/%d/%Y")
		new_date = datetime.strftime(date, "%-d-%b-%y")
    
	    # 5. write a new row of data with the transformed date and value for "approve" 
		writer.writerow([new_date, approve])

# Just done by myself, please see Abdullah's file for the in-class work