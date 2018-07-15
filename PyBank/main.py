#dependencies
import csv
import pprint
rev_change={}

# read csv
with open('budget_data.csv', mode='r', newline='') as csv_file: #opens csv file
    csv_reader = csv.DictReader(csv_file) # create reader object
    total_rev =0 #set initial revenue to 0
    months=0 #set number of months to 0
    change_profit=0 #set change in profit to 0
    prev_line= 1154293 #Set to this because the first row is skipped. Maybe find a cleaner way to do this....
    
    #print(csv_reader.fieldnames) #prints field names

    for row in csv_reader: # total net amount of months
        months +=1
        total_rev += int(row['Revenue'])
        
        #line_num = data.index(line) # gives line number as index value
        change_profit += int(row['Revenue']) - int(prev_line)
        
        if row['Date'] not in rev_change.keys(): # if Date is not in dict of rev_change, create entry
            rev_change[row['Date']] =0
            
        if row['Date'] in rev_change:# if Date exists then add change in revenue
            rev_change[row['Date']] = int(row['Revenue'])- int(prev_line)
            
        prev_line = int(row['Revenue']) #sets prev_line valuefor the next row. MUST be at the end of for loop 
    
    print('Financial Analysis')
    print('------------------------')
    maxInc='Maximum Increase in Revenue: ' + max(rev_change, key =rev_change.get) + ' (' + str(max(rev_change.values())) + ')' #max rev
    maxDec='Maximum Decrease in Revenue: ' + min(rev_change, key =rev_change.get) + ' (' + str(min(rev_change.values())) + ')' #min rev
    print('Total Months: ' + str(months))
    print('Total Revenue: $' + str(total_rev))
    print('AVG Monthly Change in Revenue: $' + str(round(change_profit/(months),2)))
    print(maxInc)
    print(maxDec)
    
with open('Results.txt','w') as txt_file: #create a new txt file and print results
    print(f'Total Months: ' + str(months), file=txt_file)
    print(f'Total Revenue: $' + str(total_rev), file=txt_file)
    print(f'AVG Monthly Change in Revenue: $' + str(round(change_profit/(months),2)), file=txt_file)
    print(str(maxInc), file=txt_file)
    print(str(maxDec), file=txt_file)