import time
import math


def max_element(l):
    max_element = 0
    for e in l:
        if e > max_element:
            max_element = e
    print  max_element


def reverse_list(l):
    print l[::-1]


def find_element(l, elem):
    for e in l:
        if e == elem:
            print 'l[%s] = %s' % (l.index(e), e)


def palindrome_string(s):
    for e in s:
        if e != s[-s.index(e) - 1]:
            print "this string is not a palindrome"
            break
        elif s.index(e) >= len(s) / 2 - 1 and e == s[-s.index(e) - 1]:
            print "this string is a palindrome"
            break


def square(l):
    li = []
    for e in l:
        if int(math.sqrt(e)) * int(math.sqrt(e)) == e:
            li.append(e)
    print li


def for_loop(l):
    sum = 0
    for e in l:
        sum += e
    print 'sum = %d' % sum


def while_loop(l):
    sum = 0
    n = 0
    while n < len(l) :
        sum += l[n]
        n += 1
    print 'sum = %d' % sum


def recursive_loop(l):
    if len(l) == 0:
        return 0
    else:
        p = l.pop()
        return recursive_loop(l) + p



start_time = time.clock()
list = [1, 2, 3, 8, 10, 8, 9, 6, 4, 16]
string = 'ab0120ba'

max_element(list)
reverse_list(list)
find_element(list, 8)
palindrome_string(string)
for_loop(list)
while_loop(list)
print 'sum = %d' % recursive_loop(list)
square(list)

print 'run_time = %s' % (time.clock() - start_time)