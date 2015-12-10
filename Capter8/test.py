import unittest
from  Capter8 import Steps, Factor,TextProcess,CodeTable

class Capter8Test(unittest.TestCase):
    def setUp(self):
        self.data_test_steps = [2, 20, 3]
        self.data_prime_or_not = [1, 2, 3, 7, 8, 9, 10, 15]
        self.data_text = "this book is mine"
        self.data_name = ["ma jinfeng", "ma  jinfeng", "  ma jinfeng  ", "jinfeng,ma", "jinfeng  , ma"
            , " jinfeng,ma  ", "ma jin feng", "jin,feng,ma"]
        self.data_table = [[1, 10], [33, 43], [250, 260], [400, 410]]

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

    def test_text_process(self):
        tp = TextProcess(self.data_text)
        print tp.count_text()
        for name in self.data_name:
            print tp.name_format(name)
        tp.show_name()

    def test_code_table(self):
        for data in self.data_table:
            tab = CodeTable(data[0], data[1])
            tab.code(data[0], data[1])
            tab.print_table()
            tab.print_code()





