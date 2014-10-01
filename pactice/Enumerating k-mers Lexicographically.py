with open("data.txt") as f:
    data = f.readlines()
    dic = data[0].strip().split()
    count = int(data[1].strip())
    # print dic, count

for x in dic:
    for y in dic:
        for z in dic:
            print ''.join([x, y, z])
