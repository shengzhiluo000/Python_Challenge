import os
import csv

# Read budget_data.csv file - Assume we dont know Pandas yet
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# open CSV file
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    # first line is header - remove first row from analysis
    header = next(csvreader)

    # Create all necessary varaible for result
    total = 0
    total_month = 0
    budgetMonth = []
    budgetList = []
    budgetChange = []
    budgetChangeMonth = []

    # Calculate total, count for months, and convert csv data into list
    for row in csvreader:
        total_month += 1
        total += int(row[1])
        budgetMonth.append((row[0]))
        budgetList.append(int(row[1]))

    # Calculate change from months and define months for that change
    for i in range(len(budgetList)):
        if i != 0:
            budgetChange.append(budgetList[i]-budgetList[i-1])
            budgetChangeMonth.append(budgetMonth[i])

    # find maximum change, minimum change, and their respective months
    for i in range(len(budgetChange)):
        if budgetChange[i] == max(budgetChange):
            BestProfitMonth = budgetChangeMonth[i]
            BestProfit = budgetChange[i]
        elif budgetChange[i] == min(budgetChange):
            WorstProfitMonth = budgetChangeMonth[i]
            WorstProfit = budgetChange[i]
        else:
            pass

# calculate for average change
Average_Change = sum(budgetChange)/len(budgetChange)

# Output:
print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total: {total}")
print(f"Average Change: {Average_Change}")
print(f"Greatest Increase in Profits: {BestProfitMonth} ({BestProfit})")
print(f"Greatest Decrease in Profits: {WorstProfitMonth} ({WorstProfit})")

text_file = os.path.join('Analysis', 'output.txt')

"output to text file"
with open(text_file,'w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------------------------\n")
    text.write(f"Total Months: {total_month}\n")
    text.write(f"Total: {total}\n")
    text.write(f"Average Change: {Average_Change}\n")
    text.write(f"Greatest Increase in Profits: {BestProfitMonth} ({BestProfit})\n")
    text.write(f"Greatest Decrease in Profits: {WorstProfitMonth} ({WorstProfit})\n")