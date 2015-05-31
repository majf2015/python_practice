def qwe(x):
	if  not isinstance(x,(int,float)):
		raise TypeError('TypeError')
	if x >= 0:
		return x
	else:
		return -x
print qwe(-9)
#print qwe('qwe')

def pri(name,age=1,city='foshan'):
	print 'name: ',name
	print 'age: ',age
	print 'city: ',city
print pri('MJF',3)

