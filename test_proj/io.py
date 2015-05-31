import os
import sys

arg = sys.argv[0]
print arg

dir_name = os.path.dirname(arg)
file_name = os.path.basename(arg)

print dir_name
print file_name

if file_name != "test.py":
    fout = open('test.py', 'w')

with open(arg, 'r') as f:
    a = f.readline()
    while a != '' :
        if file_name != "test.py":
            fout.write(a)

        if a[len(a)-1] == '\n':
            a = a[:len(a)-1]
        print a
        a = f.readline()
if file_name != "test.py":
    fout.close()

try:
    a = 'first'
    while a != 'end':
        a = raw_input("please input you word:")
        if a == 'ese':
            raise 'jj'
        print  a

except ZeroDivisionError:
    print "print type error ZeroDivisionError"
except NameError:
    print "print type rror"
finally:
    print 'a = ' + str(a)

def func2(flag):
    if (flag):
        raise "xxx"
    else:
        return 3/flag

class MyError():
    def __init__(self):
        self.__s = "my error!!!!"
    def getError(self):
        return self.__s

def func1():
    try:
       # func2(0)
        raise MyError()
    except TypeError:
        print "catch an error"
    except ZeroDivisionError:
        print "Dive by zero"
    except MyError as e:
        print e.getError()
    except:
        print "unknown error"
    return 0

func1()

