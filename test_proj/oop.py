class next1(object):
    __i = []
    __n = 0
    def __init__(self, m):
        for i in range(m):
            self.__i.append('ss' + str(i))

    def next(self):
        self.__n = self.__n + 1
        if self.__n > len(self.__i):
            raise StopIteration()
        return self.__i[self.__n - 1]


class dummy(object):
    def __init__(self, m):
        self.__m = m
        self.__s = next1(self.__m)
    def __iter__(self):
        return self.__s




d = dummy(5)
for i in d:
    print i

#for (i = d.__iter__().next(); i != StopIteration(); i = d.__iter().next())
##d.__iter__().next()
#s = d.__iter__()
#s.next()


l = ['qw', 'w', 'a', 'qa', 'ok']

for i in l:
    print i

i = 0
while i  < len(l):
    print l[i]
    i = i + 1

d = {1 : 'q', 2 : 'w', 3 : 'e'}

for k in d:
    print k
for v in d.itervalues():
    print v
for k, v in d.iteritems():
    print k , v

class dummy2(object):
    def __init__(self):
        self.__d = {}
        self.__l = []
    def insert_d(self, k, v):
        self.__d[k] = v
    def insert_l(self, ve):
        self.__l.append(ve)

    def l_in_d(self):
        for i in self.__l:
            if self.__d.has_key(i) != True:
                return False
        return True
    def key_to_l(self):
        self.__l = self.__l + self.__d.keys()
    def value_to_l(self):
        self.__l = self.__l + self.__d.values()
    def print_dl(self):
        for k, v in self.__d.iteritems():
            print k, v
        for i in self.__l:
            print i



print "my dummy2"
d2 = dummy2()
d2.insert_d(1, 'q')
d2.insert_d(4, 'qwe')
d2.insert_l(4)
d2.insert_l(6)
d2.insert_l(7)
d2.print_dl()

print d2.l_in_d()
d2.key_to_l()
d2.print_dl()
d2.value_to_l()
d2.print_dl()
