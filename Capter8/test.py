import unittest
from  Capter8 import Steps, PrimeOrNot

class Capter8Test(unittest.TestCase):
    def setUp(self):
        self.data_prime_or_not = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_steps(self):
        date = Steps()
        date.main()

    def test_prime_or_not(self):
        for num in self.data_prime_or_not:
            p = PrimeOrNot(num)
            print p.prim_or_not()

