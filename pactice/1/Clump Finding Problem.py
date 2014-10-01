##################################
##FILE NAME:        Clump Finding Problem.py 
##AUTHOR:           XIA XIAN
##DATE:                     
##VERSION:          0.1
##FUNCTION:             
###################################

line = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k = 5
L = 50
t = 4
kmer_unique = []

for i in range(0,len(line)-L+1):
    seq = line[i:i+L]
    #print seq
    kmers ={}
    for j in range(0,L-k+1):
        kmer = seq[j:j+k]
        #print kmer
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
    for (key,value) in zip(kmers.iterkeys(),kmers.itervalues()):
        if value == t:
            kmer_unique.append(key)
print ' '.join(set(kmer_unique))


