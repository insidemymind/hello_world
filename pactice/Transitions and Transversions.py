# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

from Rosalind import read_in_fasta

transition_count = 0
transversion_count = 0

data = read_in_fasta("data.txt")
seq_list = []
for key in data:
    seq_list.append(data[key])

seq1 = seq_list[0]
seq2 = seq_list[1]

for i in range(len(seq1)):
    if (seq1[i] == 'A' and seq2[i] == 'G')\
    or (seq2[i] == 'A' and seq1[i] == 'G')\
    or (seq1[i] == 'C' and seq2[i] == 'T')\
    or (seq2[i] == 'C' and seq1[i] == 'T'):
        transition_count += 1
    elif seq1[i] == seq2[i]:
        pass
    else:
        transversion_count += 1
print float(transition_count)/ transversion_count
