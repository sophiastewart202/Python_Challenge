#Modules
import os
import csv
from typing import Counter

#Specify the file to read/write to
csvpath=os.path.join('Resources','pybank_budget_data.csv')

#look in csv path
with open(csvpath) as datafile:
    #find the months column and count the total number of months by counting the rows
    next(datafile) #skip the header
    csvreader=csv.reader(datafile, delimiter=',') #open in reader mode
    total_months = sum(1 for row in csvreader)
    print(total_months)

    #find the net total amount of profits/losses over the entire period (total_months)

    #find the average of the changes in profits/losses over the entire period (total_months)

    #The greatest increase in profits (date and amount) over the entire period (total_months)

    #The greatest decrease in losses (date and amount) over the entire period (total_months)

    #print analysis to the terminal

    #export csv with results