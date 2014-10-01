from Rosalind import read_in_fasta

data = read_in_fasta("data.txt")

for x in data:
    for y in data:
        # print x, data[x][-3:], y, data[y][:3]
        if x!= y and data[x][-3:] == data[y][:3]:
            print x, y
