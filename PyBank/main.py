#Modules
import os
import csv
from typing import Counter

#Specify the file to read to
csvpath=os.path.join('Resources','pybank_budget_data.csv')

#look in csv path
with open(csvpath) as datafile:

    #Count the total number of months (by counting the rows)
    next(datafile) #skip the header
    csvreader=csv.reader(datafile, delimiter=',') #open in reader mode
    data = []
    for row in csvreader: #store each row as one item in the data list  
        data.append(row)
    total_months = sum(1 for row in data) #count all the rows
    print(total_months)

    #find the net total amount of profits/losses over the entire period
    net_total=0
    for row in data:
        net_total += int(row[1])
    print(net_total) #does python automatically know which column can be added up? Is that why this works?

    #find the average of the changes in profits/losses over the entire period (total_months)
    #IDEA 1
    revenue = []
    monthly_change = []
    for row in data:
         revenue.append(float(row[1]))
    for i in range(1,len(revenue)):
        monthly_change.append(revenue[i] - revenue[i-1])
    avg_change = sum(monthly_change)/(total_months - 1)
    avg_change = round(avg_change,2)

    #The greatest increase in profits (date and amount) over the entire period (total_months)
    # greatest_increase = max(monthly_change)
    # print(greatest_increase)

    #The greatest decrease in losses (date and amount) over the entire period (total_months)

    #print analysis to the terminal
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: $ {net_total}")
    print(f"Average Change: $ {avg_change}")

    #export csv with results