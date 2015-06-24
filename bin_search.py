

def bin_search(l, st, le, val):
    if le == 0:
        return st

    m = l[st + le / 2]
    if m == val:
        return st + le / 2
    elif m > val:
        if le / 2 <= 1:
            return st
        return bin_search(l, st, le / 2, val)
    else:
        if le / 2 == 0:
            return st
        return bin_search(l, st + le / 2 + 1, le / 2, val )


lis = [[], [1], [1, 5], [1, 5, 9], [1, 5, 9, 30], [1, 2, 5, 6, 8], [5, 5, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],\
           [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
ret = [0, 0, 1, 1, 1, 2, 1, 4, 4]
for i in range(len(lis)):
    ret_fact = bin_search(lis[i], 0, len(lis[i]), 5)
    if ret_fact == ret[i]:
        print 'success', i
    else:
        print 'error', i, ret[i], ret_fact