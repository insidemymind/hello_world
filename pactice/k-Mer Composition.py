
from itertools import product
from Rosalind import read_in_fasta_list

data = read_in_fasta_list("data.txt")[0]

kmer = {}
for i in product(['T', 'C', 'G', 'A'], repeat = 4):
    tmpkmer = ''.join(i)
    kmer[tmpkmer] = 0

for i in range(len(data)-3):
    kmer[data[i:i+4]] += 1

for key in sorted(kmer.keys()):
    print kmer[key],
