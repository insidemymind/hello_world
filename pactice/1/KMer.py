##################################
##FILE NAME:        KMer.py 
##AUTHOR:           XIA XIAN
##DATE:             11-12
##VERSION:          0.1
##FUNCTION:         find the most frequent k-mers in a string
###################################
try:
    with open("dataset_2_4.txt") as data:
        line = data.readline().strip()
        number = int(data.readline().strip())
except IOError as err:
    print 'File error: '+ str(err)

#line = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#number = 4
kmercount={}
for i in range(0,number):
    seq = line[i:]
    for j in range(0,len(seq),number):
        kmer = seq[j:j+number]
        if len(kmer) == number:
            if kmer not in kmercount:
                kmercount[kmer] = 1
            else:
                kmercount[kmer] += 1
#print kmercount
kmercount_sort = sorted(kmercount.iteritems(),key = lambda d:d[1],reverse = True)
#print kmercount_sort
maxcount = kmercount_sort[0][1]
for i in range(0,len(kmercount_sort)):
    if kmercount_sort[i][1] >= maxcount:
        print kmercount_sort[i][0],