import bubbling_sort

def bubbling_sort_test():
    lis = [[4, 6, 23, 900, 23, 5, 2, 1, 2, 5], [5, 7, 2], [6]]
    ret_lis = [[1, 2, 2, 4, 5, 5, 6, 23, 23, 900], [2, 5, 7], [6]]
    for i in range(len(lis)):
        try:
            if bubbling_sort.bubbling_sort(lis[i]) == ret_lis[i]:
                print 'success', i
            else:
                print 'error ', i, bubbling_sort.bubbling_sort(lis[i]) , ret_lis[i]
        except:
            print 'error:raise '
