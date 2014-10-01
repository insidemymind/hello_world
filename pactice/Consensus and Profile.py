def read_in_fasta(filename):
    f = open(filename)
    data = []
    for line in f:
        if line[0]=='>':
            data.append('')
        else:
            data[-1] = data[-1] + line.strip()
    return data

base = ['A','C','G','T']
filename = "data.txt"
data = read_in_fasta(filename)
count = []
for x in zip(*data):
    tmp = []
    [tmp.append(x.count(i)) for i in base]
    count.append(tmp)

string = ''
for x in count:
    string += base[x.index(max(x))]
print string
for x in zip(['A:','C:','G:','T:'],*count):
    string = [str(y) for y in x]
    print ' '.join(string)

