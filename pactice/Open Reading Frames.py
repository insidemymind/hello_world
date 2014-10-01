def read_in_fasta(filename):
    f = open(filename)
    data = []
    for line in f:
        if line[0]=='>':
            data.append('')
        else:
            data[-1] = data[-1] + line.strip()
    return data

def reverse_dna(dna):
    dna_rule = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    r_dna = ''
    for i in dna:
        r_dna += dna_rule[i]
    return r_dna[::-1]

def transcribe(dna):
    rna_rule = {'A':'U', 'G':'C', 'C':'G', 'T':'A'}
    rna = ''
    for i in dna:
        rna += rna_rule[i]
    return rna[::-1]

def translate(rna):
    translate = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'','UAC':'Y','UAG':'','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}
    protien = ''
    for i in range(len(rna)/3):
        protien += translate[rna[3*i:3*(i+1)]]
    return protien

def find_orf(rna):
    stop_codon = ['UAG', 'UGA', 'UAA']
    start_codon = 'AUG'
    orf = set()
    flag = False
    sub_flag = False
    tmp = ''
    sub_index = []
    for i in range(len(rna)/3):
        codon = rna[3*i:3*(i+1)]
        if codon in stop_codon and tmp != '':
            orf.add(translate(tmp))
            if sub_flag:
                for k in sub_index:
                    orf.add(translate(rna[k:3*i]))
            tmp = ''
            flag = False
            sub_flag = False
            sub_index = []
        elif codon == start_codon:
            if tmp == '':
                flag = True
            else:
                sub_flag = True
                sub_index.append(i*3)
            tmp += codon
        elif flag:
            tmp += codon
    # print orf
    # start = []
    # end = []
    # for i in range(len(rna)/3):
    #     codon = rna[3*i:3*(i+1)]
    #     # print codon,
    #     if codon == start_codon:
    #         start.append(3*i)
    #     elif codon in stop_codon:
    #         end.append(3*i)
    # print start, end, rna[3*i:]
    # for k in range(len(start)):
    #     # print k
    #     if len(end) - 1 >= k:
    #         while end[0] < start[k]:
    #             end = end[1:]
    #             if end == []:
    #                 break
    #         else:
    #             orf.append(rna[start[k]:end[0]])
    return orf

dna = read_in_fasta("data.txt")[0]
dna_reverse = reverse_dna(dna)
orf = set()
for k,i in enumerate([dna, dna_reverse]):
    # print k,'|',
    rna = transcribe(i)
    for j in range(3):
        [orf.add(x) for x in find_orf(rna[j:])]
print '\n'.join(orf)
