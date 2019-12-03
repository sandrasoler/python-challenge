import csv

file_to_output = "Financial_Analysis.txt"

total_months =0
total_revenue = 0
previous_revenue = 0
revenue_changes = []
revenue_dates = []

with open("budget_data.csv", "r") as revenue:
    reader = csv.DictReader(revenue)

    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row['Profit/Losses'])
            
        # Append values to revenue_changes & revenue_dates
        revenue_dif = int(row['Profit/Losses']) - previous_revenue
        revenue_dates = revenue_dates + [row['Date']]
        if previous_revenue != 0:
            revenue_changes.append(revenue_dif) 
        previous_revenue = int(row['Profit/Losses'])

greatest_increase = max(revenue_changes)
greatest_decrease = min(revenue_changes)

# Match dates to max and min revenue_changes   
x= revenue_changes.index(greatest_increase)
y= revenue_changes.index(greatest_decrease)
month_grtincrease = revenue_dates[x+1]
month_grtdecrease = revenue_dates[y+1]



print('Financial Analysis')
print ('---------------------------------------')
print('Total Months: ' + str(total_months))
print('Total:  $'+ str(total_revenue))
print('Average Change: '+str(round(int(sum(revenue_changes))/len(revenue_changes),2)))
print('Greatest Increase in Profits: ' + month_grtincrease + ' ($' + str(greatest_increase) +')')
print('Greatest Decrease in Profits: ' + month_grtdecrease + ' ($' + str(greatest_decrease) +')')



with open(file_to_output, "w+") as text_file:
    text_file.write('Financial Analysis')
    text_file.write("\n")
    text_file.write('---------------------------------------')
    text_file.write("\n")
    text_file.write('Total Months: ' + str(total_months))
    text_file.write("\n")
    text_file.write('Total:  $'+ str(total_revenue))
    text_file.write("\n")
    text_file.write('Average Change: '+str(round(int(sum(revenue_changes))/len(revenue_changes),2)))
    text_file.write("\n")
    text_file.write('Greatest Increase in Profits: ' + month_grtincrease + ' ($' + str(greatest_increase) +')')
    text_file.write("\n")
    text_file.write('Greatest Decrease in Profits: ' + month_grtdecrease + ' ($' + str(greatest_decrease) +')')