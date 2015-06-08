import math


def connect(l1, l2):
    print l1 + l2


def fibonacci(a, b):
    f = [a, b]
    for i in range(2, 10):
        f.append(a + b)
        a, b = b, f[i]
    print f


def figure(num):
    d = []
    for e in num:
        if e.isdigit():
            d.append(e)
    print d

list = [1, 2, 4, 16]
list2 = [6, 8, 9, 11]
connect(list, list2)
fibonacci(1, 2)
num = 'and456'
figure(num)