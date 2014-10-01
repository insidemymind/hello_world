instr = '17404 18011 16470 18257 17961 17180'

fields = [int(x) for x in instr.split()]
out = 2 * sum(fields[:3]) + 1.5 * fields[3] + fields[4]
print out
