#%%
import os
import csv

# Path
csvpath = os.path.join("Resources","budget_data.csv")
Ap = os.path.join("Analysis","Results.txt")

# Initialize variables to store data
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
dates = []

# Read and process the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader: # Input the rows
        date = row[0]
        profit = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount of profit/losses
        net_total += profit

        # Calculate the change in profit and store dates
        if total_months > 1:
            profit_change = profit - previous_profit
            profit_changes.append(profit_change)
            dates.append(date)

        previous_profit = profit

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_increase_date = dates[profit_changes.index(greatest_increase)]
greatest_decrease = min(profit_changes)
greatest_decrease_date = dates[profit_changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# Print the results to a txt file
with open (Ap , 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    



# %%
