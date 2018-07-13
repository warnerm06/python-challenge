import os 
import csv

# read csv
with open('budget_data.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader] #allows for mulitple for loops. Otherwise you can only use a for loop once.
    total_rev =0
    months=0
    change_profit=0
    prev_line= 1154293 #Set to this because the first row is skipped. 

    #print(csv_reader.fieldnames) #prints field names
    print('Financial Analysis')
    print('------------------------')
    for line in data: # total net amount of months
        months +=1
    print('Total Months: ' + str(months))

    for line in data: # total net amount of revenue over the entire period
        total_rev += int(line['Revenue'])
    print('Total Revenue: $' + str(total_rev))

    for line in data[1:]: # total average change in revenue from month to month
        #line_num = data.index(line) # gives line number as index value
        change_profit += int(line['Revenue']) - int(prev_line)
        prev_line = int(line['Revenue'])
   
    print('AVG Monthly Change in Revenue: $' + str(round(change_profit/len(data),2)))
 
    #index, value =max(data, key=lambda item: item['Revenue'])
    #print('Greatest Increase in Revenue: $' + str(max(data['Revenue'] for data in data))) #prints max value

    print(max(data, key=lambda x:x['Revenue']))
