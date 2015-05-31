s = [1, 2, 3, 4, 5, 6, 7, 8]
t = []

def Count():
    return len(s) * (len(s) - 1) * (len(s) - 2)

def Shu():
    for i in s:
        for j in s:
            for k in s:
                if i != j and i != k and j != k:
                    t.append(i * 100 + j * 10 + k)
    return t

print Count()

out = Shu()
print len(out)
print out