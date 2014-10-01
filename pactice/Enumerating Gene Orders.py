def permutation(li):
    if len(li) <= 1:
        yield li
    else:
        for i in permutation(li[1:]):
            for j in range(len(i) + 1):
                yield i[:j] + li[0:1] + i[j:]

num = 5
count = 1
for i in range(1,num+1):
    count *= i
print count

for i in permutation(range(1,num+1)):
    out = [str(x) for x in i]
    print ' '.join(out)
