import mysort


l = [[1, 5, 36, 67, 4, 7, 78, 100], [111, 23, 111], [1]]
result_sort = [[1, 4, 5, 7, 36, 67, 78, 100], [23, 111, 111], [1]]
result_my_reverse = [[100, 78, 7, 4, 67, 36, 5, 1], [111, 23, 111], [1]]
result_insert_sort = [[1, 4, 5, 7, 36, 67, 78, 100], [23, 111, 111], [1]]
result_add_up_sort = [[1, 4, 5, 7, 36, 67, 78, 100], [23, 111, 111], [1]]
for i in range(len(l)):
    try:
        ret_sort = mysort.select_sort(l[i])
        if ret_sort == result_sort[i]:
            print 'success', ret_sort
        else:
            print 'error1 : The %sth sorted %s is not equal to the expected result %s' % \
                  ( i, ret_sort, result_sort[i])
    except:
        print 'select sort exception:', i

    try:
        ret_my_reverse = mysort.my_reverse(l[i])
        if ret_my_reverse == result_my_reverse[i]:
            print 'success', ret_my_reverse
        else:
            print 'error2 : The %sth reversed %s is not equal to the expected result %s' % \
                  (i, ret_my_reverse, result_my_reverse[i])
    except:
        print "my_reverse exception", i

    try:
        ret_insert_sort = mysort.insert_sort(l[i])
        if ret_insert_sort == result_insert_sort[i]:
            print 'success', ret_insert_sort
        else:
            print 'error3 : The %sth sorted %s is not equal to the expected result %s' % \
                  (i, ret_insert_sort, result_insert_sort[i])
    except:
        print "insert sort exception", i

    try:
        ret_add_up_sort = mysort.add_up_sort(l[i])
        print ret_add_up_sort
        if ret_add_up_sort == result_add_up_sort[i]:
            print 'success', ret_add_up_sort
        else:
            print 'error3 : The %sth sorted %s is not equal to the expected result %s' % \
                  (i, ret_add_up_sort, result_add_up_sort[i])
    except:
        print "add_up sort exception", i






