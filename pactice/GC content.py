fhd = open('rosalind_gc.txt')

def gc_cal(line):
    n = 0
    if len(line) != 0:
        for i in line:
            if i == 'G' or i == 'C':
                n += 1
        return n*1.0/len(line)

gc_name = []
gc_content = []
seq = ''
for line in fhd:
    line = line.strip()
    if line[0] == '>':
        gc_name.append(line[1:])
        gc_content.append(gc_cal(seq))
        seq = ''
    else:
        seq += line
gc_content.append(gc_cal(seq))
gc_content = gc_content[1:]
print gc_name[gc_content.index(max(gc_content))], '\n', max(gc_content)*100


