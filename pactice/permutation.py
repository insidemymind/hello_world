def all_perms(li):
    if len(li) <=1:
        #print 'there', len(li), li
        yield li
    else:
        for k in all_perms(li[1:]):
            print 'k', k
            for i in range(len(k)+1):
                #print 'here', i, k[:i], li[0], k[i:]
                yield k[:i] + li[0:1] + k[i:]

for i in all_perms([0,1,2,]):
    print '--perm--', i
