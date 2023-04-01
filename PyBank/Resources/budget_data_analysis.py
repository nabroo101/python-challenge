import os
import csv

# assigning the file path to a variable
#budget_csv_path = os.path.join('.', 'budget_data.csv')
budget_csv_path = './Resources/budget_data.csv'
print(budget_csv_path)

with open(budget_csv_path, 'r') as csv_file:
    row_csv = csv_file.read()
    print(row_csv)
#    print(type(row_csv))

with open(budget_csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
# if data has header which it does
    header_csv = next(csv_reader)
    print(f'CSV Headers: {header_csv}')

    for row in csv_reader:
        print(row)