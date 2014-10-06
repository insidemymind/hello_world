# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

with open("data.txt") as f:
    order = f.readline().strip().split()
    n = int(f.readline().strip())

import itertools, string

tmp_order = string.lowercase[:len(order)]
all_perm = []
for i in range(1, n+1):
    all_perm.extend([''.join(p) for p in itertools.product(tmp_order, repeat=i)])


for i in sorted(all_perm):
    string = ''
    for j in i:
        string = string + order[tmp_order.index(j)]
    print string


# 感悟:
# 这道题还真的是有点tricky的.我首先想到的是用数字来替代自定义的顺序,后来为数字有两位的所困扰,后来发现自己傻了,其实用字母表就可以啊!!!string库里有26个字母的.T^T,白白花了好多时间.
