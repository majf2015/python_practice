def quick_sort(l):
    if len(l) == 0:
        raise 999
    elif len(l) == 1:
        return l
    else:
        low_list = []
        high_list = []
        middle_e = l[0]
        for i in range(len(l)):
            if i < middle_e:
                low_list.append(i)
            else:
                high_list.append(i)
        return add_list(quick_sort(low_list), quick_sort(high_list))


def add_list(l1, l2):
    pass
