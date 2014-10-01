def readFromFile(name):
    try:
        with open(name + ".txt") as data:
            genome = data.readline().strip()
            protein = data.readline().strip()
    except IOError as err:
        print 'File error: '+ str(err)
    return (genome, protein)

def translator(text):
    translate = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'','UAC':'Y','UAG':'','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}
    protein = []
    for i in range(0,len(text),3):
        protein.append(translate[text[i:i+3]])
    return ''.join(protein)

def ReverseComplement(text,verbose = True):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    comp_text = []
    for item in text:
        item = complement[item]
        comp_text.append(item)
    comp_text.reverse()
    return ''.join(comp_text)

if __name__ == "__main__":
    verbose = False
    name = 'data'
    (genome, protein) = readFromFile(name)
    genome_rc = ReverseComplement(genome, verbose)
    protein_1 = translator(genome)
    protein_2 = translator(genome_rc)

