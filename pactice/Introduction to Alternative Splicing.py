# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7


from math import factorial
n = 1741
m = 1352
comb_count = 0
for i in range(m, n+1):
    comb_count += factorial(n)/(factorial(i) * factorial(n-i))
print comb_count%1000000
