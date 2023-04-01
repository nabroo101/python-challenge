import os
import csv
print('Financial Analysis')
print('----------------------------')
# assigning the file path to a variable
budget_csv_path = os.path.join('.', 'budget_data.csv')
#budget_csv_path = './Resources/budget_data.csv'
#print(budget_csv_path)

with open(budget_csv_path, 'r', encoding="utf-8") as csv_file:
    row_csv = csv_file.read()
    #print(row_csv)
#    print(type(row_csv))

with open(budget_csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(csv_reader)
# if data has header which it does
    header_csv = next(csv_reader)
    #print(f'CSV Headers: {header_csv}')

    rows = list(csv_reader)
    total_number_of_months = len(rows)

    print(f'Total Months: {total_number_of_months}')
    #print(rows)
net_total = 0
for sub_list_profit_losses in rows:
    profit_loss = int(sub_list_profit_losses[1])
    net_total += profit_loss
print(f'Total: ${net_total}')
        
