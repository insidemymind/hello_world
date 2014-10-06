# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7


from Rosalind import read_in_fasta_list

data = read_in_fasta_list("data.txt")
n = len(data)
lenstr = len(data[0])

dist = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        diff = 0
        for k in range(lenstr):
            if data[i][k] != data[j][k]:
                diff += 1
        dist[i][j] = "%1.5f" %(float(diff)/lenstr)

for x in dist:
    print ' '.join(x)
