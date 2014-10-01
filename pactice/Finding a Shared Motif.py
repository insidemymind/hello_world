# 这个方法是有错误的，因为我没有没同时搜索其他可能的LCS，所以碰巧对了应该是“靠巧合编程”。
# 同时这个脚本有很多需要改进的地方，比如可以用动态规划和后缀树/后缀列表。
# 比如用这样的测试集就是错误的：
# >Rosalind_5905
# AAAAAF
# >Rosalind_8633
# AAAA
# >Rosalind_9525
# AF
def LCS(data, length):
    com1 = data[length.index(min(length))]
    com2 = data[0]
    lcs = LCS_2(com1, com2)
    for i in data:
        lcs = LCS_2(lcs, i)
    return lcs

def LCS_2(com1, com2):
    for i in range(len(com1),-1,-1):
        for j in range(len(com1)-i):
            com = com1[j:j+i+1]
            #print i,j,len(com1)-i,com, com2
            if com  not in com2:
                continue
            else:
                return com

f = open("data.txt")
data = []
length = []
flag = False
for line in f:
    if line[0]=='>':
        if flag:
            length.append(len(data[-1]))
        data.append('')
        flag = True
    else:
        data[-1] = data[-1] + line.strip()
length.append(len(data[-1]))
print LCS(data, length)
