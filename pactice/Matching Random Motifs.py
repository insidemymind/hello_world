# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

with open("data.txt") as f:
    n, gccontent = [float(x) for x in f.readline().strip().split()]
    string = f.readline().strip()

count_at = 0
count_cg = 0
for sub in string:
    if sub == "A" or sub == "T":
        count_at += 1
    elif  sub == "C" or sub == "G":
        count_cg += 1

print count_at, count_cg, n, gccontent
print "%1.3f" \
%(1-(1 - (gccontent/2)**count_cg*((1- gccontent)/2)**count_at)**n)


