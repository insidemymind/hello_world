with open("data.txt") as f:
    n = int(f.readline().strip())
    seta = set([int(x) for x in f.readline().strip("\n{}").split(", ")])
    setb = set([int(x) for x in f.readline().strip("\n{}").split(", ")])


setu = set(range(1, n+1))
print '{%s}' %(', '.join([str(x) for x in seta | setb]))
print '{%s}' %(', '.join([str(x) for x in seta & setb]))
print '{%s}' %(', '.join([str(x) for x in seta - setb]))
print '{%s}' %(', '.join([str(x) for x in setb - seta]))
print '{%s}' %(', '.join([str(x) for x in setu - seta]))
print '{%s}' %(', '.join([str(x) for x in setu - setb]))
