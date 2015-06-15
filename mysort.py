def my_min(l):
  if l == []:
      raise 'this is an empty list'
  else:
      min_elem  = l[0]
      for i in l:
          if min_elem > i:
              min_elem = i
  return min_elem


def my_reverse(l):
    if l == []:
        raise 999
    else:
        return l[::-1]



def my_select_sort(l):
    pass

def select_sort(l):
    if len(l) == 0:
        return []
    else:
        mysorted = []
        for i in range(len(l)):
            mysorted.append(my_min(l))
            l.remove(my_min(l))
    return mysorted


