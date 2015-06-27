def layout(l):
    le = []
    for i in l:
        le.append(len(i))

    du = max(le)
    l.insert(0, '*'*du)
    l.append('*'*du)

    for k in l:
        em = ' '* (du - len(k))
        print '*'+ k + em + '*'

l = ['e', 'er', 'err', 'error']
layout(l)