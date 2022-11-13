# Financial Records Analysis Code
# Assumptions:
#   1. Input file is in the same directory
#   2. Data is in chronological order
#   3. There are no identical increase or decrease values
# View Readme.md for Additional details

# Import dependecies

import os
import csv

# Read csv file

fpath = os.path.join("Resources","budget_data.csv") # write resource file path

# print (fpath) # Check Path

# Open file to run required operations
with open(fpath) as file:
    budget = csv.reader(file, delimiter=',')  
    budget_header = next(budget)

    # Check header
    # print(f"Budget Header: {budget_header}") 

    data = [[row[0], int(row[1])] for row in budget]

profit = [e[1] for e in data]

num = len(profit) # Number of Months
tot = int(sum(profit)) # Total of profit

profit_chg = []

# Calculate average
for e1, e2 in zip(profit[1:],profit[:-1]):
    chg = e1 - e2
    profit_chg.append(chg)
            
    # Calculate greatest increase and greatest decrease
if max(profit_chg) > 0:
    max_inc = max(profit_chg)
    date_inc = data[profit_chg.index(max_inc)+1][0]
else:
    max_inc = 'No Increase' 
    date_inc = 'N/A'   

if min(profit_chg) < 0:
    max_dec = min(profit_chg)
    date_dec = data[profit_chg.index(max_dec)+1][0]
else:
    max_dec = 'No Increase' 
    date_dec = 'N/A'   

max_dec = min(profit_chg)
d_max = profit_chg.index(max_dec)

avg_chg = round(sum(profit_chg) / len(profit_chg),2)

# Record output
output = (f'Financial Analysis \n\n'
    f'---------------------\n\n'
    f'Total Months {num} \n\n'
    f'Total: ${tot}\n\n'
    f'Average Change: ${avg_chg}\n\n'
    f'Greatest Increase in Profits: {date_inc} (${max_inc})\n\n'
    f'Greatest Decrease in Profits: {date_dec} (${max_dec})')

# Print result
print(output)


# Write output to file (over-writes existing)
with open("analysis/output.txt", "w") as f:
    print(output, file=f)