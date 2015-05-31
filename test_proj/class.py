class dog():
	def eat(self,food):
		self.__foo = "dog eat," + food
		print self.__foo

	def __init__(self, color):
		self.__coor = color

	def bar(self):
		print self.__coor, " dog barking"
		
	#def __len__(self):
	#	return 23

		

d = dog("black")
d.eat("qwe" )
d.bar()
#print "len of dog:" + str(len(d))

class BigDog(dog):
    def __init__(self, weigth):
        dog.__init__(self, "white")
        self.__w = weigth

    def bar(self):
        dog.bar(self)
        print " big dog is barking, weight:", self.__w

print "now big dog"
bd = BigDog(23)
bd.bar()












class animal():
    def __init__(self):
        print 'this is an animal'
    def walk(self, str):
        self.__s = str
        print self.__s
        print str


class cat(animal):
    def __init__(self, color):
        animal.__init__(self)
        self.__c = color
    def eat(self, food):
        self.__foo = 'cat, ' + food
        print self.__foo
	def __str__(self):
		return "cat string"

class lion(dog, cat):
    def __init__(self):
        cat.__init__(self, 'red')
        #dog.__init__(self, 'black')


print "now lion"
l = lion()
l.eat('meat')

a = animal()
a.walk("I can walk")
c = cat('red')
c.walk("red cat")
c.eat('food')

c.new_name ="whatever"

#vim
#dd
# i ->i
c2 = cat("red2")
print hasattr(c2, 'new_name')
print hasattr(c, 'new_name')

def set_name(self,name):
    self.name = name

#alt + f12
#from  types import MethodType
import types
animal.set_name = types.MethodType(set_name,None,animal)
c.set_name("feng")

c.set_name = set_name

c.set_name(c, "feng")
print c.name
print c

class human(object):
	def __init__(self, age):
		self._a = age
	def __str__(self):
		return "xxxx human"

print "now, human"
h = human(23)
#print h.__str__()
print h

#print "2" + h
#print h.get_age
#h.set_age = 27
#print h.get_age


class dummy2(object):
	def __init__(self):
		pass
	def __str__(self):
		return "xxxx"
		
d = dummy2()
print str(d)
print " 2 " + '%s' % dummy2()



