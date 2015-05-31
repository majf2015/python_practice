#dict)
d = {'q': 1, 'w': 'A', 0: 9, 8: 'S'}
print d 
print 'd[\'q\'] = '+ '%d' % (d['q'])
print 'd[\'w\'] = '+ d['w']
print 'd[0] = '+ '%d' % (d[0])
print 'd[8] = '+ d[8]

d['q'] = 'quickly'
d[8] = 12345

print d

9 in d
'qw' in d

#d.get('e')
#print d['e']

print  d.get('q')
d['r'] = 5
print d

#d.pop()
#print d
d.pop('q')
print d

s=set([1,1,1,2,3,4,'q','w'])
s.add(5)
s.add(5)
print s
s.remove('q')
print s
s1=set([1,2,'a','s'])
print s & s1
print s | s1

a="qwertyuip123"
print a.replace('123','asdffgh')
print a
# absolute value,
