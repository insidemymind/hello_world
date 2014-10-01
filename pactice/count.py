line = open('rosalind_dna.txt').readline()  #rosalind_dna.txt
count = [0,0,0,0] # 0-A, 1-C, 2-G, 3-T
for i in line.strip():
    #print i
    if i =='A':
        index = 0
    elif i == 'C':
        index = 1
    elif i == 'G':
        index = 2
    elif i == 'T':
        index = 3
    count[index] += 1
count = [str(x) for x in count]
print ' '.join(count)
