# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

def count_floor(string, obj):
    cnt = 0
    # print string[:string.find(obj)]
    for i in string[:string.find(obj)]:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1

    # cnt2 = 0
    # for j in string[string.find(obj):]:
    #     if j == ")":
    #         cnt2 += 1
    #     elif j == "(":
    #         cnt2 -= 1

    # assert cnt == cnt2
    return cnt



tree = []
pair = []
with open("data.txt") as f:
    count = 0
    for line in f:
        count += 1
        if count % 3 == 1:
            tree.append(line.strip())
        elif count % 3 == 2:
            pair.append(line.strip().split())

for i, t in enumerate(tree):
    print sum([count_floor(t, pair[i][0]), count_floor(t, pair[i][1])]),
