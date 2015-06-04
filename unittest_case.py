def unittest_case(k, m):
    def y(x):
        if x % 2 == 0:
            return -1.0 / (2 * x - 1)
        else:
            return 1.0 / (2 * x - 1)

    l = map(y, range(1, k))
    add = 0
    for i in l:
        add += i
    print 'y =:', 4 * add
    if 4 * add - m < 0.00001:
        print "right"
    else:
        print "error"

print 'test:', 8.0/3
unittest_case(3, 8.0/3)

print 'test:', 52.0/15
unittest_case(4, 52.0/15)