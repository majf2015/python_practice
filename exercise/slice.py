list1 = range(1,6)
list2 = [12,13,14,15]
print list1[: 3] + list2[-3: ]
for v in list1:
	print v

i = 0
while i < len(list1):
	print list1[i]
	i = i + 1

d1 = {1:'a',2:'b', 3:'c'}
for key, val in d1.iteritems():
	print key
	print val
	
print [x for x in range(0,11)]
print [x for x in list1 if x%3 == 0]


import os
print os.listdir(".") # ..

g = (x for x in range(0,101))

#1 2 3 4 .... [ hello 31
for i in g:
	print i
	if i % 30 == 0:
		print 'hello\n'
		
		
g = (x * 2 for x in [1,2,3,4,5] if x * 2 % 6 != 0 )
for i in g:
	print i
	

print "generator test"

def print_even(list):
	for value in list:
		if value % 2 == 0:
			yield value


# function == first class citizen.		
f = print_even

def man_func(f):
  f(range(1,5))
 
 
	
#print_even(list2)
p = print_even(list2)
print p.next()
print p.next()

#print print_even.next()	

