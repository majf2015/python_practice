# encoding:utf-8
import time
import math


#---查找数列中最大的元素---
def max_element(l):
    max_element = 0
    for e in l:
        if e > max_element:
            max_element = e
    print  max_element


#---反转数列---
def reverse_list(l):
    print l[::-1]


#---查找指定的元素是否在数列中---
def find_element(l, elem):
    for e in l:
        if e == elem:
            print 'l[%s] = %s' % (l.index(e), e)


#---回文---
def palindrome_string(s):
    if len(s) == 0:
        print "this string is empty"
    else:
        for e in s:
            if e != s[-s.index(e) - 1]:
                print "this string is not a palindrome"
                break
            elif s.index(e) >= len(s) / 2 - 1 and e == s[-s.index(e) - 1]:
                print "this string is a palindrome"
                break


#---查找数列中前20位完全平方数---
def square(l):
    li = []
    for e in l:
        if int(math.sqrt(e)) * int(math.sqrt(e)) == e and len(li) < 20:
            li.append(e)
    print li


#---for循环求数列中元素的和---
def for_loop(l):
    sum = 0
    for e in l:
        sum += e
    print 'sum = %d' % sum


#---while循环求数列中元素的和---
def while_loop(l):
    sum = 0
    n = 0
    while n < len(l) :
        sum += l[n]
        n += 1
    print 'sum = %d' % sum


#---递归循环求数列中元素的和---
def recursive_loop(l):
    if len(l) == 0:
        return 0
    else:
        p = l.pop()
        return recursive_loop(l) + p


#---主运行程序，计算运行时间---
start_time = time.clock()
list = [1, 2, 3, 8, 10, 8, 9, 6, 4, 16]
string = ''

max_element(list)
reverse_list(list)
find_element(list, 8)
palindrome_string(string)
for_loop(list)
while_loop(list)
print 'sum = %d' % recursive_loop(list)
square(list)

print 'run_time = %s' % (time.clock() - start_time)