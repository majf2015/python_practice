import re



class Steps:
    def __init__(self):
        self.fro = 0
        self.fto = 0
        self.step = 0
        self.steps = []

    def main(self):
        self.input()
        self.get_steps()
        self.range_test()

    def input(self):
        try:
            self.fro = int(raw_input("enter the starting number"))
            self.fto = int(raw_input("enter the end number"))
            self.step = int(raw_input("enter the step number"))
        except:
            print "please enter right number"


    def get_steps(self):
        self.steps = range(self.fro, self.fto, self.step)
        return self.steps

    def range_test(self):
        range_test1 = range(10)
        range_test2 = range(3, 19, 3)
        range_test3 = range(-20, 861, 220)
        return range_test1, range_test2, range_test3

class Factor:
    def __init__(self, num):
        self.num = num
        self.factors = set([1, self.num])
        self.prime_factors = []
        self.count = self.num / 2

    def prim_or_not(self, num):
        count = num / 2
        while count > 1:
            if num % count == 0:
                return False
            count -= 1
        return True

    def get_factors(self):
        count = self.num / 2
        while count > 1:
            if self.num % count == 0:
                self.factors.add(count)
                self.factors.add(self.num / count)
                count -= 1
            else:
                count -= 1
        return self.factors

    def get_prime_factors(self, num):
        count = num / 2
        if self.prim_or_not(num):
            return self.prime_factors
        else:
            while count > 1:
                if num % count == 0:
                    self.prime_factors.append(num / count)
                    if self.prim_or_not(count):
                        self.prime_factors.append(count)
                        return self.prime_factors
                    else:
                        return self.get_prime_factors(count)
                count -= 1

    def perfect_or_not(self):
        if self.prim_or_not(self.num):
            return False
        else:
            factors = list(self.get_factors())
            count = 0
            for i in factors:
                count += i
            if count == 2 * self.num:
                return True
            else:
                return False

    def get_N(self, num):
        N = 1
        for i in range(1, num + 1):
            N = N * i
        return N

    def fibonacci(self, n):
        a, b , i= 1, 1, 3
        fib = [1, 1]
        while i <= n:
            a, b = b, a + b
            fib.append(b)
            i += 1
        return fib

class TextProcess:
    def __init__(self, text):
        self.text = text
        self.name = []

    def count_text(self):
        count_u, count_f, count_w = 0, 0, 0
        s = re.compile("\w")
        for word in self.text:
            if word in "aeiouAEIOU":
                count_u += 1
            elif s.match(word):
                count_f += 1
        count_w = len(self.text.split())
        return count_u, count_f, count_w

    def name_format(self, name):
        if  re.match( r"^ *[a-zA-Z]+ *, *[a-zA-Z]+ *$", name):
            self.name.append("".join(name.split()))
            return 1
        elif re.match( r"^ *[a-zA-Z]+ *[a-zA-Z]+ *$", name):
            self.name.append("%s,%s" % (name.split()[1], name.split()[0]))
            return 0
        else:
            return -1

    def input(self):
        num = raw_input("Enter total number of names:")
        wrong_time = 0
        for n in num:
            name = raw_input("Please enter name %d" % n)
            if self.name_format(name) == 0:
                wrong_time += 1
                print "Wrong format... should be Last, First."
                print "You have done this %d time(s) already. Fixing input..." % wrong_time

    def show_name(self):
        print "The sorted list (by last name) is:"
        for name in self.name:
            print name

class CodeTable:
    def __init__(self, begi, en):
        self.begin = begi
        self.end = en
        self.dec = []
        self.count_chr = 0
        self.lenth = 0

    def input(self):
        try:
            beg = int(raw_input("Enter begin value:"))
            e = int(raw_input("Enter end value:"))
        except:
            print "begin/end must integer"
            self.input()

        if beg > e:
            print "begin must lest then end"
            self.input()
        else:
            self.begin = beg
            self.end = e

    def code(self, begin, end):
        for num in range(begin, end + 1):
            if num < 0 or num > 255:
                self.dec.append([num, bin(num), oct(num), hex(num)])
            else:
                self.dec.append([num, bin(num), oct(num), hex(num), chr(num)])
                self.count_chr += 1

    def print_code_table(self):
        if self.count_chr != 0:
            print "DEC     BIN     OCT     HEX     "
            print "--------------------------------"
            for row in self.dec:
                print row[0],row[1],row[2],row[3]











