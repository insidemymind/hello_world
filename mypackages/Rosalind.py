def read_in_fasta(filename):
    f = open(filename)
    data = {}
    for line in f:
        if line[0]=='>':
            name = line[1:].strip()
            data[name] = ''
        else:
            data[name] = data[name] + line.strip()
    return data

FILENAME = "data.txt"
DNA_RULE = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
RNA_RULE = {'A':'U', 'G':'C', 'C':'G', 'T':'A'}
PROTEIN_WEIGHT = {'A':71.03711,
'C':103.00919,
'D':115.02694,
'E':129.04259,
'F':147.06841,
'G':57.02146,
'H':137.05891,
'I':113.08406,
'K':128.09496,
'L':113.08406,
'M':131.04049,
'N':114.04293,
'P':97.05276,
'Q':128.05858,
'R':156.10111,
'S':87.03203,
'T':101.04768,
'V':99.06841,
'W':186.07931,
'Y':163.06333}
TRANSLATE = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'','UAC':'Y','UAG':'','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}
