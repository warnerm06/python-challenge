#dependencies
import csv 
import os 
import pprint

file_path= 'election_data.csv'

with open(file_path, mode='r', newline ='') as csvfile: #opens csv file
    csv_reader=csv.DictReader(csvfile) # reads csv file
    count =0 #initial count of votes
    candidates={} # dict of candidats. Initially it is empty but will be filled from csv
    
    for row in csv_reader:
        count +=1 #tallies total vote count
        if (row['Candidate']) not in candidates.keys(): # if candidate is not in dict of candidates create entry
            candidates[row['Candidate']]=0 #creates entry and sets default value (votes) to 0
                 
        if (row['Candidate']) in candidates:# if candidate exists then add a vote
            candidates[row['Candidate']] +=1   

    #print results
    
    print('Election Results')
    print('---------------------')
    print('Total Votes: ' + str(count)) #total count of entries in csv
    print('---------------------')
        
    for k, v in candidates.items(): #print each candidate and votes in dict
        print(k + ': '+ str('{:.1%}'.format(v/count)) + ' ('+str(v) +')')
    print('---------------------')
    maxvotes='Winner: ' + max(candidates, key =candidates.get) #max votes in candidates dict
    print(maxvotes)
    
    # text file output
with open('Electrion_Results.txt','w') as txt_file: #create a new txt file and pint results
    print(f'Election Results', file=txt_file)
    print(f'---------------------', file=txt_file)
    print(f'Total Votes: {count}', file=txt_file)
    print(f'---------------------', file=txt_file)
    for k, v in candidates.items():
        print(k + ': '+ str('{:.1%}'.format(v/count)) + ' ('+str(v) +')', file=txt_file)
    print(f'---------------------', file=txt_file)
    print(f'{maxvotes}', file=txt_file)
    
    
    