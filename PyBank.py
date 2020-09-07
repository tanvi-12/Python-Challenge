#import modules
import os
import csv
import datetime

#create pathway
budget_csv = os.path.join("..", "Python-Challenge", "budget_data.csv")

#data stores
monthcount = 0
total = 0
currentmonth = 0
prevmonth = 0
change = [0]

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip header
    csv_header=next(csv_file)

    for row in csv_reader:
        
        #combine months
        monthcount += 1
        #total
        total = total + int(row[1])
        #find current month
        currentmonth = int(row[1])
        if (monthcount > 1):
            change.append(currentmonth - prevmonth)
            if (change[monthcount-1] == max(change)):
                maxchange = (f"Greatest Increase in Profits: {str(row[0])} ${max(change)}")
            if (change[monthcount-1] == min(change)):
                minchange = (f"Greatest decrease in Profits: {str(row[0])} ${min(change)}")
        prevmonth = currentmonth
    ave_change = sum(change)/(monthcount-1)


#print outputs
Results = (f"""Financial Analysis
----------------------------
Total Months: {monthcount}
Total: ${total}
Average Change: ${ave_change}
{maxchange}
{minchange}""")


#print outputs - text file

file = open( "ElectionAnalysis.txt", "w")
file.write(Results)
file.close()
