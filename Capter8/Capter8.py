class Steps:
    def __init__(self):
        self.fro = 0
        self.fto = 0
        self.step = 0
        self.steps = []

    def main(self):
        self.input()
        print self.get_steps()
        print self.range_test()

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

class PrimeOrNot:
    def __init__(self, num):
        self.num = num

    def prim_or_not(self):
        count = self.num / 2
        while count > 1:
            if self.num % count == 0:
                count -= 1
                return False
            else:
                return True



