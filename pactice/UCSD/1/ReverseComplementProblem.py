##################################
##FILE NAME:        ReverseComplementProblem.py
##AUTHOR:           XIA XIAN
##DATE:             11-12
##VERSION:          0.1
##FUNCTION:
###################################

data = 'CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT'
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
comp_data = []
for item in data:
    item = complement[item]
    comp_data.append(item)
comp_data.reverse()
print ''.join(comp_data)
