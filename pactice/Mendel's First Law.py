fhd = open('rosalind_iprb.txt')
(k, m, n) = fhd.readline().strip().split()
k = int(k)
m = int(m)
n = int(n)
total = sum([k, m, n])

result = 1 - 1.0* 1/total * 1/(total - 1)* (0.25 * m *m - 0.25*m + m*n + n*n - n)

print result
