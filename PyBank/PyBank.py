# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path("budget_data.csv")
output_file = Path("budget_analysis.txt")

# Declare the lists and variables to be used
total_months = 0
month_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["",999999999]
total_net = 0

# Open the csv file as an object
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    # Extract first row
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])
    
    # Looping over each row
    for row in csvreader:
        
        # Updateding totals
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        
        # Updated the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list.append(net_change)
        month_change = month_change.append(row[0])
        
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
        # Calculaye the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
# Calculate the average net change
net_monthly_average = round(sum(net_change_list)/len(net_change_list),2)
            
# Export results to txt file
with open(output_file,"w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${net_monthly_average}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
        