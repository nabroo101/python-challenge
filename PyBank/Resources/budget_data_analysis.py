import os
import csv
print('Financial Analysis')
print('----------------------------')
total_net = 0
# assigning the file path to a variable
budget_csv_path = os.path.join('.', 'budget_data.csv')


with open(budget_csv_path, 'r', encoding="utf-8") as csv_file:
    row_csv = csv_file.read()
   

with open(budget_csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
# if data has header which it does
    header_csv = next(csv_reader)
    rows = list(csv_reader)

# ==============================================
# calculating total number of months  
total_number_of_months = len(rows)
print(f'Total Months: {total_number_of_months}')

# ==============================================
#calculating the total net profit
for sublist in rows :
    total = int(sublist[1])
    total_net = total_net + total
print(f'Total: ${total_net}')

#===============================================
#calculating th average change
#defineing monthly changes as an empty list because we will be adding the profit changes in it
monthly_changes = []
previous_month_profit = int(rows[0][1])
for i in range(1, len(rows)):
#     #current month profit will be the month after the first which will have index of [i] and we itrating starting from the second element of the list
#     #the row[1] means we are looking at the value profit inside the sublist[[month0,value0]<==i=0,[month1,value1]<==i=1,[month2,value2]i<== 2 ....]===>[]
     current_month_profit = int(rows[i][1])
#     #monthly change will be the value of the current month - previous month will be taking the previous value and it will take the value of the current
#     #because the current one will be the previous one in the next itration
     monthly_change = current_month_profit - previous_month_profit
#     #we need to save those changes in a list which i called monthly_changes and we add values by calling the .append function which adds the new values to the list.
     monthly_changes.append(monthly_change)
#     #now we define the previous month profit by assigning it to the current month
     previous_month_profit = current_month_profit
# #calculating the average *note we -1 from the total number of moths because the first month value has no previos value !!
average_monthly_change = sum(monthly_changes) / (total_number_of_months - 1)
rounded_average_change = round(average_monthly_change, 2)
print(f'Average Change: ${rounded_average_change}')

#==================================================================
#The greatest increase in profits (date and amount) over the entire period
#we use the max modual to calculate the value from the monthly_changes list that we previously created
greatest_increase_value = max(monthly_changes)
greatest_decrease_value = min(monthly_changes)
#because the monthly_changes index starts from the second index , we need to add one to the index
greatest_increase_date_index = monthly_changes.index(greatest_increase_value)+1
greatest_decrease_date_index = monthly_changes.index(greatest_decrease_value)+1
#we go back to the original list so we can retrive the date from the index we just got for both min and max
max_date = rows[greatest_increase_date_index]
min_date = rows[greatest_decrease_date_index]

print(f'Greatest Increase in Profits: {max_date[0]} (${greatest_increase_value})')
print(f'Greatest Decrease in Profits: {min_date[0]} (${greatest_decrease_value})')
    

        
        
        
        





