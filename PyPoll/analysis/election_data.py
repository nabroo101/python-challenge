import os
import csv

# assiging the path of the csv file to a variable
election_csv_path = r"C:\Users\Lenovo\unc\homework\python-challenge\PyPoll\Resources\election_data.csv"

with open(election_csv_path, 'r', encoding='utf-8') as csv_file:
    row_csv = csv_file.read()

with open(election_csv_path, 'r') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    #if data has headers 
    header_csv = next(csv_reader)
    data_csv_list = list(csv_reader)

#=======================================================================================================
print('Election Results')
print('------------------------')

#total number of votes can be calculated by the modual len

number_votes=len(data_csv_list)
print(f'Total Votes: {number_votes}')
print('----------------------')

#=======================================================================================================

#creating an empty dic
candidate_with_votes = {}
for i in data_csv_list:
    candidate = i[2]
    if candidate in candidate_with_votes:
        candidate_with_votes[candidate] += 1
    else:
        candidate_with_votes[candidate] = 1


for candidate, votes in candidate_with_votes.items():
    vote_percentage = votes / number_votes * 100
print(f'{candidate}: {vote_percentage:.3f}% ({votes})')

winner =''
max_votes = 0
for candidate, votes in candidate_with_votes.items(): 
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print('-------------------------')       
print(f'Winner: {winner}')
print('-------------------------')
#with open('C:\\Users\\Lenovo\\unc\\homework\\python-challenge\\PyPoll\\analysis\\output.txt', 'w') as file: 