import os
import csv

### Creating Path to CSV File
csvpath = os.path.join('..', 'PyBank','Resources','budget_data.csv')

### Opening CSV File
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader, None) #Iterating Over Header

### Counting the Number of Months
    totalMonths = 0
### Counting the Net Profit/Losses
    netProfit = 0

### Looping through Dataset
    for row in csvreader:
        totalMonths += 1 ### Calculating total number of months
        netProfit += int(row[1]) ### Calculating net profit/loss
        ### Finding the Last Value of Dataset
        lastProfit = row[1]

    


    

        

#profitChange = lastProfit -
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${netProfit}')
    print(lastProfit)
    #print(firstProfit)

