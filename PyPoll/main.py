### Creating a Function to Make Script User Friendly and Universal
def electionAnalysis(electionCSV, candidate1, candidate2, candidate3, candidate4):

    ### Importing Modules
    import os
    import csv

    ### Creating Path to CSV File
    csvpath = os.path.join('..', 'PyPoll','Resources',electionCSV)

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
    candidate1Count = 0 #Number of Votes Candidate 1 Received
    candidate2Count = 0 #Number of Votes Candidate 2 Received
    candidate3Count = 0 #Number of Votes Candidate 3 Received
    candidate4Count = 0 #Number of Votes Candidate 4 Received
    winner = 0 #Greatest Number of Votes

    ### Calculating a List of Candidates Who Recieved Votes
    for i in range(totalVotes):
        if candidate[i] == candidate1:
            candidate1Count = candidate1Count + 1
        elif candidate[i] == candidate2:
            candidate2Count = candidate2Count + 1
        elif candidate[i] == candidate3:
            candidate3Count = candidate3Count + 1
        elif candidate[i] == candidate4:
            candidate4Count = candidate4Count + 1

    ### Determining Winner
    if candidate1Count > winner:
        winner = candidate1Count
        winnerName = candidate1
    elif candidate2Count > winner:
        winner = candidate2Count
        winnerName = candidate2
    elif candidate3Count > winner:
        winner = candidate3Count
        winnerName = candidate3
    elif candidate4Count > winner:
        winner = candidate4Count
        winnerName = candidate4

    ### Calculating Percentages to Two Decimal Places
    candidate1Per = format((candidate1Count/totalVotes)*100, '.2f')
    candidate2Per = format((candidate2Count/totalVotes)*100, '.2f')
    candidate3Per = format((candidate3Count/totalVotes)*100, '.2f')
    candidate4Per = format((candidate4Count/totalVotes)*100, '.2f')

    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {totalVotes}')
    print('-------------------------')
    print(f'{candidate1}: {candidate1Per}% ({candidate1Count})')
    print(f'{candidate2}: {candidate2Per}% ({candidate2Count})')
    print(f'{candidate3}: {candidate3Per}% ({candidate3Count})')
    print(f"{candidate4}: {candidate4Per}% ({candidate4Count})")
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
        text.write(f'{candidate1}: {candidate1Per}% ({candidate1Count})\n')
        text.write(f'{candidate2}: {candidate2Per}% ({candidate2Count})\n')
        text.write(f'{candidate3}: {candidate3Per}% ({candidate3Count})\n')
        text.write(f"{candidate4}: {candidate4Per}% ({candidate4Count})\n")
        text.write('-------------------------\n')
        text.write(f'Winner: {winnerName}\n')
        text.write('-------------------------')

    print(f'A Text File with the Results has been Exported to: {txtpath}')

### Prompting the User to Input the Town's Election CSV File
print("Input the Company's Budget CSV File")
x = input()
print("Input Candidate 1.")
x1 = input()
print("Input Candidate 2.")
x2 = input()
print("Input Candidate 3.")
x3 = input()
print("Input Candidate 4.")
x4 = input()
electionAnalysis(x,x1,x2,x3,x4)