# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7


edge = 0
with open("data.txt") as f:
    n = int(f.readline().strip())
    for line in f:
        edge += 1

print n - edge - 1
