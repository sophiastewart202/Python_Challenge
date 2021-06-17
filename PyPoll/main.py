#Modules
import os
import csv

#Specify the file to read/write to
csvpath=os.path.join('Resources','pypoll_election_data.csv')

#look in csv path
with open(csvpath) as text
    #The total number of votes cast (total_votes = count # of voter ID)

    #A complete list of candidates who received votes (Candidates = empty list, 
    # for every distinct value in column 3, append value to list)

    #The percentage of votes each candidate won (percentage_votes = count of votes per candidate/total_votes)

    #The total number of votes each candidate won (votes_won = count of occurences of each distinct value 
    # in Candidate column)

    #The winner of the election based on popular vote (winner = greatest votes_won)

    #print analysis to the terminal 
    # title = "Election Results"
    # (print("title") 
    # print(f'Total Votes: {total_votes}')
    # For every Candidate in Candidates:
    # print(f'| Candidate: {percentage_votes} %, ({votes_won})')

    #export csv (as text file) to analysis folder with results
