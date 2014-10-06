# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

from Rosalind import read_in_fasta_list

data = read_in_fasta_list("data.txt")

chromosome = data[0]
del(data[0])
while 1:
    if len(data) == 0:
        break
    else:
        for read in data:
            if len(read) % 2 == 0: # read length is even.
                for length in range(len(read)/2, 0, -1):
                    # print read, read[:len(read)/2+length], len(read)/2+length, read[len(read)/2-length:], len(read)/2-length
                    if read[:len(read)/2+length] in chromosome:
                        chromosome = chromosome + read[len(read)/2+length:]
                        data.remove(read)
                        break
                    elif read[len(read)/2-length:] in chromosome:
                        chromosome = read[:len(read)/2-length]+chromosome
                        data.remove(read)
                        break
            else:
                for length in range(len(read)/2+1, 0, -1):
                    # print read, read[:len(read)/2+length], len(read)/2+length, read[len(read)/2-length+1:], len(read)/2-length+1
                    if read[:len(read)/2+length] in chromosome:
                        chromosome = chromosome + read[len(read)/2+length:]
                        data.remove(read)
                        break
                    elif read[len(read)/2-length+1:] in chromosome:
                        chromosome = read[:len(read)/2-length+1]+chromosome
                        data.remove(read)
                        break

print chromosome
