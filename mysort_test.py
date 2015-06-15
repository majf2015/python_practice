import mysort

try:
    l = [[1, 5, 36, 67, 4, 7, 78, 100], [], [111, 23,111], [1]]
    result_sort = [[1, 4, 5, 7, 36, 67, 78, 100], [], [23, 111, 111], [1]]
    result_my_reverse = [[100, 78, 7, 4, 67, 36, 5, 1], [], [111, 23, 111], [1]]
    for i in range(len(l)):
        ret_sort = mysort.select_sort(l[i])
        ret_my_reverse = mysort.my_reverse(l[i])
        if ret_sort == result_sort[i]:
            print 'success', ret_sort
        else:
            print 'error : The %sth sorted %s is not equal to the expected result %s' %  ( i, ret_sort, result_sort[i])

        if ret_my_reverse == result_my_reverse[i]:
            print 'success', ret_my_reverse
        else:
            print 'error : The %sth reversed %s is not equal to the expected result %s' %  ( i, ret_my_reverse, result_my_reverse[i])
except:
    print 'this is an empty list'