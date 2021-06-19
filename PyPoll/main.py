#Modules
import os
import csv

#Specify the file to read/write to
csvpath=os.path.join('Resources','pypoll_election_data.csv')

#look in csv path
with open(csvpath) as datafile:
    next(datafile) #skip headers
    csvreader = csv.reader(datafile, delimiter=',') #open in reader mode
    data = [] #list of data, row by row
    id = [] #list of voters by id
    county = [] #county list
    candidates = [] #candidates list

    for row in csvreader:
        data.append(row)

        id.append(row[0])

        if row[1] not in county:
            county.append(row[1])

        if row[2] not in candidates:
            candidates.append(row[2])

    #The total number of votes cast
    total_votes = int(len(id))

    #The number of votes and percentage of votes each candidate won 
    def Election_Results():
        results = {}
        results_list = []
        votes_won = 0
        #find the vote count for each candidate
        for candidate in candidates:
            for row in data:
                if candidate in row:
                    votes_won += 1
        
            percentage_votes = round((votes_won/total_votes)*100,3)
            print(f'{candidate}: {votes_won}, {percentage_votes} %')

            #add candidate results to dictionary
            results[votes_won] = candidate
            #reset vote count
            votes_won = 0

        all_keys = results.keys()
        winning_vote = max(all_keys)
        winner = str(results[winning_vote])
        print("--------------------------")
        print(f'Winner: {winner}')
          

    #The winner of the election based on popular vote (winner = greatest votes_won)

    #Create a dictionary
    #look up winner by max(votes_won)

    #print analysis to the terminal 
    print("Election Results")
    print("--------------------------") 
    print(f'Total Votes: {total_votes}')
    print("--------------------------")
    Election_Results()
    print("--------------------------")

    #export csv (as text file) to analysis folder with results
