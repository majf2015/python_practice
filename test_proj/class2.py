class Baseclass(object):
    def __init__(self,k):
        self.__k = k
        self.__v = 1
    def printself(self):
        print self.__k, self.__v
    def getVelue(self):
        return self.__k, self.__v

class Deriveclass(Baseclass):
    def __init__(self):
        Baseclass.__init__(self, "first")
        a, b = self.getVelue()
        self.__L = str(a) + str(b)

    def printL(self):
        print self.__L

A = Deriveclass()
A.printself()
A.printL()

import os
lis = os.listdir('..')
print lis