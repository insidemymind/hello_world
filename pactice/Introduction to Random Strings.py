# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

from math import log10

with open("data.txt") as f:
    string = f.readline().strip()
    list_a = [float(x) for x in f.readline().strip().split()]


count_at = 0
count_cg = 0
for sub in string:
    if sub == "A" or sub == "T":
        count_at += 1
    else:
        count_cg += 1

for a in list_a:
    print "%1.3f" %(count_at*log10((1-a)/2) + count_cg*log10(a/2)),
