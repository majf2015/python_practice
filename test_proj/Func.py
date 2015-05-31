
def map2(f, lst):
    l = []
    for i in lst:
        l.append(f(i))
    return l

def def_func(y):
    def dec_func(f):
        return lambda (x): f(x) + y
    return dec_func

@ def_func(3)
def func2(x):
    return x * 2

@ def_func(4)
def func3(x):
    return x * 3


print func2(2)
print func3(4)
print map2(func2, [2, 4, 6, 8])