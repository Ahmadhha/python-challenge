# Vote Analysis Code
# Assumptions:
#   Input file is in a /Resources folder in the same directory
#  
# View Readme.md for Additional details

# Import dependecies

import os
import csv

# Read csv file
fpath = os.path.join("Resources","election_data.csv") # write resource file path

# Column of Candidates Name
NAME = 2

# Open file to run required operations
with open(fpath) as file:
    votes = csv.reader(file, delimiter=',')  
    votes_header = next(votes)
    
    # Declare dictionary fo results
    results = {}
    
    # Identify Unique candidates and tally votes
    for row in votes:
        if row[NAME] not in results:
            results[row[NAME]] = 0
        results[row[NAME]] += 1

# Caclulate total votes
total_votes = sum(results.values())

# Calculate percentage
results_percentage = {key: round(value / total_votes * 100, 3) for key, value in results.items()}

# Find Winner
winner = max(results, key=results.get)

# Print Results to Command line
output1 = (f'Election results\n\n'
    '--------------------------\n\n'
    f'Total Votes: {total_votes}\n\n'
    '--------------------------\n')

print(output1)

for key1, value2 in results.items():
    
    print(f'{key1}: {results_percentage[key1]}% ({value2})\n')

output3 = (f'--------------------------\n\n'
    f'Winner: {winner}')

print(output3)

# Write Results to file
with open("analysis/output.txt", "w") as f:
    print(output1, file = f)
    for key1, value2 in results.items():
        print(f'{key1}: {results_percentage[key1]}% ({value2})\n', file = f)
    print(output3, file = f)

    




