def comb(lst, n):
    """
    combination with generetor.
    """
    length = len(lst)
    if n == 1:
        for x in lst:
            yield [x]
    else:
        for y in range(length):
            tmp = lst[0]
            lst = lst[1:]
            # print y, tmp
            for k in comb(lst, n-1):
                # print k
                yield [tmp] + k


def perm(lst, n):
    """
    permutation with generator.
    """
    length = len(lst)
    if n == 1:
        for x in lst:
            yield [x]
    else:
        for y in range(length):
            tmp = lst[0]
            lst = lst[1:]
            for k in perm(lst, n-1):
                for z in range(len(k)+1):
                    yield k[:z] + [tmp] + k[z:]


def different_perm(lst, n):
    """
    permutation with repeat.
    """
    length = len(lst)
    if n == 1:
        for x in lst:
            yield [x]
    else:
        for y in range(length):
            tmp = lst[y]
            lst = lst
            for k in perm(lst, n-1):
                yield [tmp] + k


if __name__ == '__main__':
    for i in comb(range(4), 4):
        print '--comb--', i

    for i in perm(range(3), 3):
        print '--perm--', i

    for i in different_perm(range(3), 3):
        print '--diff_perm--', i
