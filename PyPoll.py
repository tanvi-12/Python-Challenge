import os
import csv
import collections
from collections import Counter

election_csv = os.path.join("..", "Python-Challenge", "election_data.csv")

votes = []
candidates = ["Khan","Correy","Li","O'Tooley"]

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #reader
    csv_header=next(csv_file)
    for row in csv_reader:
        #combine votes
        votes.append(row[0])
         #combine candidates
        candidates.append(row[2])

    #count number of votes for each candidate    
    a = dict(Counter(candidates)) #dictionary
    
    Khan = int(a["Khan"]-1)
    Correy = int(a["Correy"]-1)
    Li = int(a["Li"]-1)
    OTooley= int(a["O'Tooley"]-1)

    #find percentage of votes
    pk = '{:.3%}'.format(Khan/len(votes))
    pc = '{:.3%}'.format(Correy/len(votes))
    pl = '{:.3%}'.format(Li/len(votes))
    po = '{:.3%}'.format(OTooley/len(votes))

    #find winner
    winner = max(a, key=a.get)

#create result variable
Results = (f"""Election Results
-------------------------
Total Votes: {len(votes)} 
-------------------------
Khan: {pk} ({Khan})
Correy: {pc} ({Correy}) 
Li: {pl} ({Li})
O'Tooley: {po} ({OTooley})
-------------------------
Winner: {winner} 
-------------------------""")

#print outputs - text file

file = open( "PollingAnalysis.txt", "w")
file.write(Results)
file.close()



