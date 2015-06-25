def quick_sort(l):
    if len(l) <= 0:
        return l
    else:
        low_list = []
        high_list = []
        middle_e = l[0]
        for i in range(1, len(l)):
            if l[i] < middle_e:
                low_list.append(l[i])
            else:
                high_list.append(l[i])
        low_list = quick_sort(low_list)
        low_list.append(middle_e)
        high_list = quick_sort(high_list)

    return low_list + high_list



