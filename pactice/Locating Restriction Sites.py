def read_in_fasta(filename):
    f = open(filename)
    data = []
    for line in f:
        if line[0]=='>':
            data.append('')
        else:
            data[-1] = data[-1] + line.strip()
    return data

filename = "data.txt"
data = read_in_fasta(filename)[0]
dna_rule = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
pos = []
for i in range(len(data)-2):
    if data[i] == dna_rule[data[i+1]]:
        for k in range(1,6):
            if i-k >=0 and i+k+1 <= len(data)-1\
            and data[i-k] == dna_rule[data[i+k+1]]:
                pos.append([i-k+1, 2+2*k])
            else:
                break
    else:
        continue

pos.sort(key=lambda tup: tup[0])

for x in pos:
    print x[0],x[1])

