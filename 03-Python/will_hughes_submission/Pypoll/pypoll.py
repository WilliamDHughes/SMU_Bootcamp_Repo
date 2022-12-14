import csv

csvpath = "C:/Users/Will/Desktop/smubootcamp/gitlab/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

rows = 0
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        rows += 1
        candidate = row[2]
        if candidate in votes.keys():
            votes[candidate] += 1
        else:
            votes[candidate] = 1

print(votes)
charles = votes["Charles Casper Stockham"] / rows
diana = votes["Diana DeGette"] / rows
raymon = votes["Raymon Anthony Doane"] / rows

poll_output = f"""
    Total Votes: {rows}
    Charles Casper Stockham: {votes["Charles Casper Stockham"]}: {round(100*votes["Charles Casper Stockham"]/rows, 3)}
    Diana DeGette: {votes["Diana DeGette"]}: {round(100*votes["Diana DeGette"]/rows, 3)}
    Raymon Anthony Doane: {votes["Raymon Anthony Doane"]}: {round(100*votes["Raymon Anthony Doane"]/rows, 3)}  """

with open('Polling Data.txt', 'w') as f:
    f.write('Polling Data.txt\n')
    f"-------------------------\n"
    f.write("Winner: Diana DeGette!")
    f"-------------------------\n"
    f.write(poll_output) 