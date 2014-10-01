##################################
##FILE NAME:        Approximate Pattern Matching Problem.py 
##AUTHOR:           XIA XIAN
##DATE:             11-15 
##VERSION:          0.1
##FUNCTION:         
###################################

try:
    with open("data.txt") as data:
        pattern = data.readline().strip()
        text = data.readline().strip()
        mismatch = int(data.readline().strip())
        answer = [int(item) for item in data.readline().strip().split()]
except IOError as err:
    print 'File error: '+ str(err)

myans = []
for i in range(0,len(text)-len(pattern)+1):
    temp = text[i:(i+len(pattern))]
    mis = 0
    #print temp,pattern
    for j in range(0,len(temp)):
        if mis > mismatch:
            break
        elif temp[j] != pattern[j]:
            mis += 1
    if mis <= mismatch:
        print i,
