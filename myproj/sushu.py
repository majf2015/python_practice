import math


class  SuShu(object):
    def __init__(self):
        self.shu = []
        self.sushu = []

    def GetSuShu(self):
        self.shu = range(int(raw_input('enter one number')) + 1)
        i = len(self.shu) - 1
        while i != 0:
            j = 2
            while j != 0 :
                if i % j == 0:
                    if i == 2:
                        self.sushu.append(2)
                    j = 0
                elif j > math.sqrt(i):
                    self.sushu.append(i)
                    j = 0
                else:
                    j += 1
            i -= 1
        print self.sushu

shu = SuShu()
shu.GetSuShu()





