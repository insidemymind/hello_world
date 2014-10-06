# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7


# 这道题的关键就在于怎么看待 "随机字符串中出现目标子字符串" 这件事
# 应该的解决方法就是:
# 去看一个长度为n的字符串有多少个位置可以出现长度为m的子串?
# 长度为m的子串有多大的概率是目标字符串?
# 然后两个的概率相乘,就可以得到结果了.

# 参考了一下网址上的解决方法, 非常感谢jschendel写的非常清楚的代码
# https://github.com/jschendel/Rosalind/blob/dff803987c240ab846a21307d234e7506327e680/047_EVAL.py

with open("data.txt") as f:
    data = f.readlines()
    n = int(data[0].strip())
    m = len(data[1].strip())
    gc_list = [float(x) for x in data[2].strip().split()]
    sub = data[1].strip()

from Rosalind import string_count

gc_count = string_count(sub, 'G') + string_count(sub, 'C')
at_count = len(sub) - gc_count

pos_count = n - m + 1

for gc in gc_list:
    probility = (gc*0.5)**gc_count*((1-gc)*0.5)**at_count
    print "%1.3f" %(probility*pos_count),

