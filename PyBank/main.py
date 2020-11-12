### Importing Modules
import os
import csv

### Creating Path to CSV File
csvpath = os.path.join('..', 'PyBank','Resources','budget_data.csv')

### Opening CSV File
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader, None) #Iterating Over Header

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

### Setting Variables to Zero
netProfit = 0 # Total Net Profit
greatInc = 0 # Greatest Increase 
greatDec = 0 # Greatet Decrease

for i in range(totalMonths): # Setting Range to totalMonths Since Data and Profit are Same Length
### Calculating Total Net Profit
    netProfit = netProfit + int(Profit[i])

### Calculating Greatest Profit Increase/Decrease    
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
print(f'Greatest Decrease in Profits: {DecDate} ({greatDec})\n')

### Creating Text File
txtpath = os.path.join('..', 'PyBank','Analysis','budget_data_results.txt')

with open(txtpath, 'w') as text:
    text.write('Financial Analysis \n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {totalMonths}\n')
    text.write(f'Total: ${netProfit}\n')
    text.write(f'Average Change: {AvgChange}\n')
    text.write(f'Greatest Increase in Profits: {IncDate} ({greatInc})\n')
    text.write(f'Greatest Decrease in Profits: {DecDate} ({greatDec})\n')

print(f'A Text File with the Results has been Exported to: {txtpath}')