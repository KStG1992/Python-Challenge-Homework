import os
import csv

### Creating Path to CSV File
csvpath = os.path.join('..', 'PyBank','Resources','budget_data.csv')

### Opening CSV File
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader, None) #Iterating Over Header

### Counting the Net Profit/Losses
    netProfit = 0
### Date Array
    Data = []
### Profit Array
    Profit = []

### Looping through Dataset
    for row in csvreader:
        Data.append(row[0])
        Profit.append(row[1])

### Calculating total number of months
totalMonths = len(Data)

### Calculating net profit/loss (Condense Loop)
for row in Profit:
    netProfit += int(row)

### Calculating Greatest Profit Increase/Decrease
greatInc = 0
greatDec = 0
for i in range(len(Profit)- 1): #think about later
    initial = Profit[i-1]
    final = Profit[i]
    change = int(final) - int(initial)

    if change > greatInc:
        greatInc = change
        IncDate = Data[i]
    elif change < greatDec:
        greatDec = change
        DecDate = Data[i]

### Calculating Average Change
finalProfit = int(Profit[totalMonths - 1])
firstProfit = int(Profit[0])
periodChange = finalProfit - firstProfit
AvgChange = round(periodChange / (totalMonths - 1),2)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${netProfit}')
print(f'Average Change: {AvgChange}')
print(f'Greatest Increase in Profits: {IncDate} ({greatInc})')
print(f'Greatest Decrease in Profits: {DecDate} ({greatDec})')

