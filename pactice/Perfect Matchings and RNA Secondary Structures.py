# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7


# 求RNA序列匹配的perfect matching 个数
# 实际上就是 (AU对个数的阶乘 * GC对个数的阶乘)

from math import factorial
from Rosalind import read_in_fasta

all_data = read_in_fasta("data.txt")
for key in all_data:
    data = list(all_data[key])
    num_a = data.count('A')
    num_c = data.count('C')

    print factorial(num_a) * factorial(num_c)
