d = {}
with open('ip.txt', 'r') as f:
    for line in f.readlines():
        ip = line.split()[0]
        if ip in d.iterkeys():
            d[ip] += 1
        else:
            d[ip] = 1
for k, v in d.iteritems():
    print k, v