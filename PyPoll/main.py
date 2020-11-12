### Importing Modules
import os
import csv

### Creating Path to CSV File
csvpath = os.path.join('..', 'PyPoll','Resources','election_data.csv')

### Opening CSV File
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader, None) #Iterating Over Header
    
### Creating Arrays    
    voterID = []
    candidate = []

    ### Looping through Dataset
    for row in csvreader:
        voterID.append(row[0])
        candidate.append(row[2])

### Calculating total number of months
totalVotes = len(voterID)

### Setting Variables to Zero
khanCount = 0 #Number of Votes Khan Received
correyCount = 0 #Number of Votes Correy Received
liCount = 0 #Number of Votes Li Received
otooleyCount = 0 #Number of Votes O'Tooley Received
winner = 0 #Greatest Number of Votes

### Calculating a List of Candidates Who Recieved Votes
for i in range(totalVotes):
    if candidate[i] == 'Khan':
        khanCount = khanCount + 1
    elif candidate[i] == 'Correy':
        correyCount = correyCount + 1
    elif candidate[i] == 'Li':
        liCount = liCount + 1
    elif candidate[i] == "O'Tooley":
        otooleyCount = otooleyCount + 1

### Determining Winner
if khanCount > winner:
    winner = khanCount
    winnerName = 'Khan'
elif correyCount > winner:
    winner = correyCount
    winnerName = 'Correy'
elif liCount > winner:
    winner = liCount
    winnerName = 'Li'
elif otooleyCount > winner:
    winner = otooleyCount
    winnerName = "O'Tooley"

### Calculating Percentages to Two Decimal Places
khanPer = format((khanCount/totalVotes)*100, '.2f')
correyPer = format((correyCount/totalVotes)*100, '.2f')
liPer = format((liCount/totalVotes)*100, '.2f')
otooleyPer = format((otooleyCount/totalVotes)*100, '.2f')

print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalVotes}')
print('-------------------------')
print(f'Khan:     {khanPer}% ({khanCount})')
print(f'Correy:   {correyPer}% ({correyCount})')
print(f'Li:       {liPer}% ({liCount})')
print(f"O'Tooley: {otooleyPer}% ({otooleyCount})")
print('-------------------------')
print(f'Winner: {winnerName}')
print('-------------------------\n')

### Creating Text File
txtpath = os.path.join('..', 'PyPoll','Analysis','election_data_results.txt')

with open(txtpath, 'w') as text:
    text.write('Election Results \n')
    text.write('----------------------------\n')
    text.write(f'Total Votes: {totalVotes}\n')
    text.write('----------------------------\n')
    text.write(f'Khan: {khanPer}% ({khanCount})\n')
    text.write(f'Correy: {correyPer}% ({correyCount})\n')
    text.write(f'Li: {liPer}% ({liCount})\n')
    text.write(f"O'Tooley: {otooleyPer}% ({otooleyCount})\n")
    text.write('-------------------------\n')
    text.write(f'Winner: {winnerName}\n')
    text.write('-------------------------')

print(f'A Text File with the Results has been Exported to: {txtpath}')  