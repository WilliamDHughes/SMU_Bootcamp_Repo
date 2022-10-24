import csv
csvpath = "C:/Users/Will/Desktop/smubootcamp/gitlab/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

rows = 0
total = 0
last_profit = 0
total_changes = 0
num_changes = 0 #85 expected

max_change = -99999999999
min_change = 99999999999
min_month = ""
max_month = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        rows += 1 
        total += int(row[1])

        if rows == 1:
            last_profit = int(row[1])
        else:
            change = int(row[1]) - last_profit
            total_changes += change
            num_changes += 1

            if (change > max_change):
                max_change = change
                max_month = row[0]
            elif (change < min_change):
                min_change = change
                min_month = row[0]
            else:
                pass
            avg_change = total_changes / num_changes 
        #reset      
        last_profit = int(row[1])  
         

# print(rows)
# print(total)
# print(num_changes)
# print(total_changes / num_changes)
# print(f"Max Change: {max_month}: {max_change}")
# print(f"Min Change: {min_month}: {min_change}")

output = f"""
    Total Months: {rows}
     Total: {total}
    Average Change: {avg_change}
    Greatest Increase in Profits: {max_month}: {max_change}
    Greatest Decrease in Profits: {min_month}: {min_change}"""

with open('Financial Analysis.txt', 'w') as f:
    f.write('Financial Analysis.txt')
    f.write(output)
