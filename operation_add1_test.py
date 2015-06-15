import operation



add1 = ['33', '232', '9999']
add2 = ['232',  '99', '8888888']
result = ['265', '331', '1']
for i in range(len(add1)):
    if operation.add1(add1[i], add2[i]) != result[i]:
        print 'error : The %sth addition %s is not equal to the expected result %s' %  ( i, operation.add1(add1[i], add2[i]), result[i])
    else:
        print 'success'

