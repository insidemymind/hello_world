# 这个表达更好：
# uniprot = "http://www.uniprot.org/uniprot/%s.fasta"
# f = urlopen(uniprot % protein).read().decode('utf-8')
# f = ''.join(f.splitlines()[1:])
def fetch_fasta(web):
    import urllib2
    response = urllib2.urlopen(web)
    html = response.read()
    line = html.split('\n')
    line = [x.strip() for x in line]
    title, seq = line[0], ''.join(line[1:])
    return seq

def read_in(filename):
    fhd = open(filename)
    seqs = []
    pro_name = []
    for line in fhd:
        protein = line.strip()
        pro_name.append(protein)
        seqs.append(fetch_fasta('http://www.uniprot.org/uniprot/' + protein+ '.fasta'))
    return pro_name, seqs

import re
motif = re.compile(r'N[^P][ST][^P]')
pro_name, seqs = read_in("data.txt")
for k, i in enumerate(seqs):
    loc = [0]
    flag = True
    seq = i
    count = 0
    while flag:
        try:
            m = re.search(motif, seq)
            index = m.start()
            loc.append(loc[-1]+index + 1)
            seq = seq[index+1:]
            count += 1
        except AttributeError:
            flag = False
    if len(loc) != 1:
        loc = [str(x) for x in loc]
        print pro_name[k], '\n', ' '.join(loc[1:])


