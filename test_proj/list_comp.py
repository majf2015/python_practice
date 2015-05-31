# (x,y,z)
# 0 < x, y, z < 100
#print [(x, y, z) for x in range(0, 101) for y in range(0, 101) for z in range(0, 101) if x != y and x != z and y != z]

x1 = [11, 12, 13, 14]
x2 = [21, 22, 23, 24]
x3 = [31, 32 ,33, 34]

a  = [x1, x2, x3]

print [[j for j in range(i, i + 4) ] for i in range(11, 32, 10)]
print [[j + i for j in range(1, 5)] for i in range(10, 31, 10)]

s1 = {1, 3, 5, 7}
s2 = {3, 5, 8, 9}
s3 = s1 ^ s2
print s3
l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3]
l3 = zip(l1, l2)
print l3

ss = "x{{0}}x{1}x"
h = 9
print ss.format(1, h, 2)
print ss

g = (x for x in range(1, 10))
print g.next()

for i in g:
    print i


a, b, c= 'ffh', 'qw','ws'
print a

#from 20150104 import map2, reduce2
import sys
sys.path.append('D:\\python')
import mapmap
m = mapmap.map2(lambda x :x**2, x1)
print  m
#print [[x for x in range(11, 15)], [y for y in range(21, 25)], [z for z in range(31, 35)]]

print '111111111111111111111111'
import os
os.path.dirnam