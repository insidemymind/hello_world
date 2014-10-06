# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

from math import factorial

n=975

comb_count = 0
for i in range(1, n+1):
    comb_count += factorial(n)/(factorial(i) * factorial(n-i))
comb_count += 1
print comb_count%1000000


# 更好的解决方法:
print 2**n % 1000000
