def is_greater_than_15(x):
	if x >= 15:
		return True
	else:
		return False

def is_greater_than_15_2(x):
	return x >= 15,x, 
	
def dummy_func(x):
	pass

def default_arg_func(gender, name = "feng"):
	print name, gender

def print_argument(*x):
	for xx in x:
		print xx

print_argument(2,3,4,6)

print is_greater_than_15(100)
print is_greater_than_15_2(100)
print is_greater_than_15_2(10)
x1,x2 = is_greater_than_15_2(100)
x3 = is_greater_than_15_2(23)

print x1,x2,x3

default_arg_func('feng',"male")


print dummy_func(2)


def keyword_func(name, gender, **kw):
	print "name:", name, "gender:", gender, "kw:", kw
	

d1 = {'age':23}
keyword_func("feng", "male", age = '25')
keyword_func("feng", "male", age = 25, city = 'shenzheng', height = 150)


#define 

# 1 argument: N, 1 + 2 + 3 + .... + N
def sum_to_n(n, sum):
	if n > 0:
		return sum_to_n(n-1, sum + n)
	return sum
	
#print sum_to_n(2,0) = sum_to_n(1, 2)=sum_to_n(0,3)=3
print sum_to_n(3,0)
