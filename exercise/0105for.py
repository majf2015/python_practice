
#dog.py

#print 'The quick brown for',"jumps over",'the lazy dog'
a = "abb"
b = "cc"
if a == b:
    print '1234'
else:
    print 'qwer'
input = []

flag = True
while flag:
	a=raw_input("please input your words:\n")
	input.append(a)		
	flag =  input[-1] != 'end'

i = 1
out = ""
for b in input:
	out=out + b + '%d' % (i)
	i =  i + 1	
print out   
#print "%s www %s" % ()

# "23" -> int
