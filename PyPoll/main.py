import csv
import os

# Read budget_data.csv file - Assume we dont know Pandas yet
election_data = os.path.join("Resources", "election_data.csv")

# open CSV file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # first line is header - remove first row from analysis
    header = next(csvreader)

    # Create all necessary varaible for result
    total = 0
    count_Charles = 0
    count_Diana = 0
    count_Raymon = 0

    # count total votes and individual's total
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
    
# create dictionary for result later
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

text_file = os.path.join('Analysis', 'output.txt')

# output to text file
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