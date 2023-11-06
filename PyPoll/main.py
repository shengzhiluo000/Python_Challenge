import csv
import os

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # first line is header - remove first row from analysis
    header = next(csvreader)

    total = 0
    count_Charles = 0
    count_Diana = 0
    count_Raymon = 0

    for row in csvreader:
        total += 1
        if row[2] == "Charles Casper Stockham":
            count_Charles += 1
        elif row[2] == "Diana DeGette":
            count_Diana += 1
        elif row[2] == "Raymon Anthony Doane":
            count_Raymon += 1
        else:
            pass
    
    # ref: https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    vote_dict = {"Charles Casper Stockham":count_Charles,
                 "Diana DeGette":count_Diana,
                 "Raymon Anthony Doane":count_Raymon}

# return result with maximum vote using zip function
result = max(zip(vote_dict.values(), vote_dict.keys()))[1]

# Test:
print("Election Results")
print("-------------------------------------------")
print(f"Total Votes: {total}")
print("-------------------------------------------")
print(f"Charles Casper Stockham: {count_Charles/total:.03%} ({count_Charles})")
print(f"Diana DeGette: {count_Diana/total:.03%} ({count_Diana})")
print(f"Raymon Anthony Doane: {count_Raymon/total:.03%} ({count_Raymon})")
print("-------------------------------------------")
print(f"Winner: {result}")
print("-------------------------------------------")

# ref https://www.pythontutorial.net/python-basics/python-write-text-file/

text_file = os.path.join('Analysis', 'output.txt')

"output to text file"
with open(text_file,'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------------------------\n")
    text.write(f"Total Votes: {total}\n")
    text.write("-------------------------------------------\n")
    text.write(f"Charles Casper Stockham: {count_Charles/total:.03%} ({count_Charles})\n")
    text.write(f"Diana DeGette: {count_Diana/total:.03%} ({count_Diana})\n")
    text.write(f"Raymon Anthony Doane: {count_Raymon/total:.03%} ({count_Raymon})\n")
    text.write("-------------------------------------------\n")
    text.write(f"Winner: {result}\n")
    text.write("-------------------------------------------")