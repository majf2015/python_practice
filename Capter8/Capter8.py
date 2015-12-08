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
    def __init__(self):

