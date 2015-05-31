d = {'name': 'feng', 'age': 27, 'gender': 'male'}
for key in d:
	print key
for value in d.itervalues():
	print value
for v in d.iteritems():
	print v
for age in 'age':
	print age

from collections import Iterable
print isinstance('qwe', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for key, value in enumerate([1,2,3,4,5]):
	print key, value
	
range_make = [(x + 1 * y * y - k for x in range(2, 5) for y in range(2, 4) for k in range(3, 7)]
print range_make, len(range_make)