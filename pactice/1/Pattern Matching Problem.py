##################################
##FILE NAME:        Pattern Matching Problem.py 
##AUTHOR:           XIA XIAN
##DATE:              
##VERSION:          0.1
##FUNCTION:         
###################################

pattern = 'ATAT'
data = "GATATATGCATATACTT"

for i in range(len(data)-len(pattern)+1):
    kmer = data[i:i+len(pattern)]
    if kmer == pattern:
        print i,