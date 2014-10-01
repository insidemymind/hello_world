def read_in_fasta(filename):
    f = open(filename)
    data = []
    for line in f:
        if line[0]=='>':
            data.append('')
        else:
            data[-1] = data[-1] + line.strip()
    return data

data = read_in_fasta("data.txt")
dna = data[0]
sub = data[1]
print dna, sub
index = 0
index_list = []
for i in sub:
    print i, dna[index:]
    tmp = dna[index:].index(i)
    index_list.append(str(tmp + index + 1))
    index += tmp + 1
print ' '.join(index_list)
