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

def kmersFound(text,k):
    for i in range(0,len(text)-k+1):
        tmp = text[i:(i+k)]
        if tmp in kmers:
            kmers[tmp] += 1
        else:
            kmers[tmp] = 1

def ReverseComplement(text):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    comp_text = []
    for item in text:
        item = complement[item]
        comp_text.append(item)
    comp_text.reverse()
    return ''.join(comp_text)

if __name__ == "__main__":
    name = "dataset_8_5"
    (text,k,mismatch) = readFromFile(name)
    kmers = {}
    print type(text),text
    text_rc = ReverseComplement(text)
    kmersFound(text,k)
    kmersFound(text_rc,k)
    print kmers


#diction = {}
#for i in kmers:
#    value = 0
#    for j in kmers:
#        if i != j and mismatchs(i,j) <= mismatch:
#            value += kmers[j]
#    value += kmers[i]
#    diction[i] = value
#
#kmers_sort = sorted(diction.iteritems(),key = lambda d:d[1],reverse = True)
##print kmercount_sort
#maxcount = kmers_sort[0][1]
#for i in range(0,len(kmers_sort)):
#    if kmers_sort[i][1] >= maxcount:
#        print kmers_sort[i][0],
#
