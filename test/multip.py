def multiply(m):
    for i in range(1, m+1):
        for j in range(1, i+1):
            if i == j:
                print '%d * %d = %-3d' % (j, i, i*j)
            else:
                print '%d * %d = %-3d' % (j, i, i*j),


multiply(9)