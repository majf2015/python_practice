import unittest
from  Capter8 import Steps, Factor

class Capter8Test(unittest.TestCase):
    def setUp(self):
        self.data_test_steps = [2, 20, 3]
        self.data_prime_or_not = [1, 2, 3, 7, 8, 9, 10, 15]

    def test_steps(self):
        print "test_steps"
        date = Steps()
        date.fro = self.data_test_steps[0]
        date.fto = self.data_test_steps[1]
        date.step = self.data_test_steps[2]
        print date.get_steps()
        print date.range_test()

    def test_number(self):
        for num in self.data_prime_or_not:
            p = Factor(num)
            print 'test number', num
            print 'prime:',p.prim_or_not(num)
            print 'factors:',p.get_factors()
            print 'prime_factors:',p.get_prime_factors(num)
            print 'perfect_or_not:',p.perfect_or_not()
            print 'get_N:', p.get_N(num)
            print 'fibonacci:', p.fibonacci(num)

