def translator(text):
    translate = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'','UAC':'Y','UAG':'','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}
    protein = []
    for i in range(0,len(text),3):
        protein.append(translate[text[i:i+3]])
    return ''.join(protein)

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
data = read_in_fasta(filename)
seq = data[0]
#print data
for i in data[1:]:
    if i in seq:
        pos = seq.index(i)
        seq = seq[0:pos] + seq[pos+len(i):]
#print seq
newseq = ''
for i in range(len(seq)):
    if seq[i] =='T':
        newseq += 'U'
    else:
        newseq += seq[i]
#print newseq

print translator(newseq)
