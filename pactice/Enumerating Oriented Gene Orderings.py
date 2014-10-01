# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

import copy
from permutation2 import perm, comb

num = 5

count = 0
for i in perm([str(x) for x in range(1,num+1)], num):
# i: 所有可能的排列,没有符号
    for j in range(0, num+1):# j: 需要考虑加几个负号
        if j == 0:
            print ' '.join(i)
            count += 1
        else:
            for k in comb(range(num), j):# k: 负号的位置是哪里
                tmp_i = copy.deepcopy(i)
                for pos in k:
                    tmp_i[pos] = '-'+tmp_i[pos]
                print ' '.join(tmp_i)
                count += 1

print count

