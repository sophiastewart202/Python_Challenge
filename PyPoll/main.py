#Modules
import os
import csv

#Specify the file to read/write to
csvpath=os.path.join('Resources','pypoll_election_data.csv')

#look in csv path
with open(csvpath) as datafile:
    next(datafile) #skip headers
    csvreader = csv.reader(datafile, delimiter=',') #open in reader mode
    id = []
    county = []
    candidates = []

    for row in csvreader:

        id.append(row[0])

        if row[1] not in county:
            county.append(row[1])

        if row[2] not in candidates:
            candidates.append(row[2])

    #The total number of votes cast
    total_votes = int(len(id))
    print(total_votes)

    #A complete list of candidates who received votes
    print(candidates)

    #The percentage of votes each candidate won (percentage_votes = count of votes per candidate/total_votes)


    #The total number of votes each candidate won (votes_won = count of occurences of each distinct value 
    # in Candidate column)

    #The winner of the election based on popular vote (winner = greatest votes_won)

    #print analysis to the terminal 
    # title = "Election Results"
    # (print("title") 
    # print(f'Total Votes: {total_votes}')
    # for every Candidate in Candidates:
    #   print(f'| Candidate: {percentage_votes} %, ({votes_won})')

    #export csv (as text file) to analysis folder with results
