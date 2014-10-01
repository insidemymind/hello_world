#!/usr/bin/env
def readFromFile(name):
    try:
        with open(name + ".txt") as data:
            (text) = data.readline().strip().split()[0]
            (k,mismatch) = data.readline().strip().split()
    except IOError as err:
        print 'File error: '+ str(err)
    return (str(text),int(k),int(mismatch))

def mismatchs(k1,k2):
    mis =0
    for i in range(0,len(k1)):
        if k1[i] != k2[i]:
            mis +=1
    return mis

def kmersFound(text,k,verbose = True):
    for i in range(0,len(text)-k+1):
        tmp = text[i:(i+k)]
        kmers[tmp] += 1
    if verbose:
        print kmers

def ReverseComplement(text,verbose = True):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    comp_text = []
    for item in text:
        item = complement[item]
        comp_text.append(item)
    comp_text.reverse()
    return ''.join(comp_text)

def dictionFound(kmers,mismatch,verbose = True):
    diction = {}
    for i in kmers:
        value = 0
        for j in kmers:
            if i != j and mismatchs(i,j) <= mismatch:
                value += kmers[j]
        value += kmers[i]
        diction[i] = value

    kmers_sort = sorted(diction.iteritems(),key = lambda d:d[1],reverse = True)
    if verbose:
        print diction,"\n",kmers_sort
    maxcount = kmers_sort[0][1]
    kmersMaxcount = []
    for i in range(0,len(kmers_sort)):
        if kmers_sort[i][1] >= maxcount:
            kmersMaxcount.append(kmers_sort[i][0])
    return kmersMaxcount

def translator(binstr,k):
    kmer = []
    translate = {'00':'A', '01':'C', '10':'G', '11':'T'}
    for i in range(0,k*2,2):
        string = binstr[i] + binstr[i+1]
        kmer.append(translate[string])
    return ''.join(kmer)

def kmerGenerator(k):
    for i in range(0,4**9):
        binstr = str(bin(i))[2:]
        if len(binstr) < k*2:
            binstr = '0'*(k * 2 - len(binstr)) + binstr
        kmers[translator(binstr,k)] = 0

if __name__ == "__main__":
    verbose = False
    name = "dataset_8_5"
    (text,k,mismatch) = readFromFile(name)
    kmers = {}
    kmerGenerator(k)
    kmersFound(text,k,verbose)
    text_rc = ReverseComplement(text,verbose)
    kmersFound(text_rc,k,verbose)
    for i in dictionFound(kmers,mismatch,verbose):
        print i,
