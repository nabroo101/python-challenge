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