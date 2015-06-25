import quick_sort


l = [[1, 5, 36, 67, 4, 7, 78, 100], [111, 23, 111], [1], []]
result_sort = [[1, 4, 5, 7, 36, 67, 78, 100], [23, 111, 111], [1], []]
for i in range(len(l)):
    try:
        ret_sort = quick_sort.quick_sort(l[i])
        if ret_sort == result_sort[i]:
            print 'success', ret_sort
        else:
            print 'error1 : The %sth sorted %s is not equal to the expected result %s' % \
                  ( i, ret_sort, result_sort[i])
    except:
        print 'select sort exception:', i



