def quick_sort(l):
    if len(l) == 0:
        raise 999
    elif len(l) == 1:
        return l
    else:
        low_list = []
        high_list = []
        middle_e = l[0]
        for i in l:
            if i < middle_e:
                low_list.append(i)
            else:
                high_list.append(i)
        low_list = quick_sort(low_list)
        high_list = quick_sort(high_list)

    return add_list(low_list, high_list)


def add_list(l1, l2):
    re_sorted = []
    if len(l1) != 0:
        for i in l1:
            re_sorted.append(i)
    if len(l2) != 0:
        for j in l2:
            re_sorted.append(j)
    return re_sorted


