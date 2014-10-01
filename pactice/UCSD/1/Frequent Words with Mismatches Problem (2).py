#!/usr/bin/env 
try:
    with open("data.txt") as data:
        (text,k,mismatch)=data.readline().strip().split()
except IOError as err:
    print 'File error: '+ str(err)

def mismatchs(k1,k2):
    mis =0
    for i in range(0,len(k1)):
        if k1[i] != k2[i]:
            mis +=1
    return mis

k = int(k)
mismatch = int(mismatch)

kmers = {}
for i in range(0,len(text)-k+1):
    tmp = text[i:(i+k)]
    if tmp in kmers:
        kmers[tmp] += 1
    else:
        kmers[tmp] = 1

dump = []
diction = {}
for i in kmers:
    for j in kmers:
        if j not in dump and i != j and mismatchs(i,j) <= mismatch:
            value = kmers[i] + kmers[j]
            diction.update({i:value})
            dump.append(j)
print dump
print diction
kmers_sort = sorted(diction.iteritems(),key = lambda d:d[1],reverse = True)
#print kmercount_sort
maxcount = kmers_sort[0][1]
for i in range(0,len(kmers_sort)):
    if kmers_sort[i][1] >= maxcount:
        print kmers_sort[i][0],