# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

from math import factorial

n = 84
m = 9
mod = 1000000

print (factorial(n) / factorial(n-m))%mod
