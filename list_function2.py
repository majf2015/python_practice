# encoding:utf-8
import math


#---连接---
def connect(l1, l2):
    print l1 + l2


#---斐波那契---
def fibonacci(a, b):
    f = [a, b]
    for i in range(2, 10):
        f.append(a + b)
        a, b = b, f[i]
    print f


#---获取数字---
def figure(num):
    d = []
    for e in num:
        if e.isdigit():
            d.append(e)
    print d


#---交替合并---
def interchange_combine(l1, l2):
    n = 1
    for e in l2:
        l1.insert(n, e)
        n += 2
    print l1




#---主运行程序---
list = [1, 2, 4, 16]
list2 = [6, 8, 9, 11,12]

interchange_combine(list, list2)
connect(list, list2)
fibonacci(1, 2)
num = 'and456'
figure(num)
