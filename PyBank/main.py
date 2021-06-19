#Modules
import os
import csv
import sys

#Specify the file to read to
csvpath = os.path.join('Resources','pybank_budget_data.csv')

#look in csv path
with open(csvpath) as datafile:

    #Count the total number of months (by counting the rows)
    next(datafile) #skip the header
    csvreader = csv.reader(datafile, delimiter=',') #open in reader mode
    data = []
    for row in csvreader: #store each row as one item in the data list  
        data.append(row)
    total_months = sum(1 for row in data) #count all the rows

    #find the net total amount of profits/losses over the entire period
    net_total = 0
    for row in data:
        net_total += int(row[1])

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

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(monthly_change)
    greatest_increase = round(greatest_increase)

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(monthly_change)
    greatest_decrease = round(greatest_decrease)

    #Create date list
    date = []
    for row in data:
        date.append(row[0])

    #Look up the dates of the greatest increase and decrease in profits
    grtst_incr_date = str(date[monthly_change.index(greatest_increase)])
    grtst_dcrs_date = str(date[monthly_change.index(greatest_decrease)])

    #create function to print analysis to the terminal
    def financial_report():
        print("-----------------------------------")
        print("Financial Analysis")
        print("-----------------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total Revenue: $ {net_total}")
        print(f"Average Change: $ {avg_change}")
        print(f"Greatest Increase in Profits: {grtst_incr_date} $ {greatest_increase}")
        print(f"Greatest Decrease in Profits: {grtst_dcrs_date} $ {greatest_decrease}")
    
    #print to terminal
    financial_report()

    #Specify the file to write to
    output_path = os.path.join("analysis", "financial_analysis.txt")

    #export text file with results
    with open(output_path,'w') as text:
        sys.stdout = text
        financial_report()
        text.close()
