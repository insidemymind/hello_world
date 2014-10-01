# rna_rule = {'A':'U', 'G':'C', 'C':'G', 'T':'A'}
dna_rule = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
line = open('rosalind_revc.txt').readline().strip()
newline = ''
# for i in line:
#     if i == 'T':
#         newline +=  'U'
#     else:
#         newline += i
# print newline

for i in line:
    newline += dna_rule[i]
print newline[::-1]
