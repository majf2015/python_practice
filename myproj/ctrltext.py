import math
import wx


class  SuShu(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "SuShu Frame")
        self.shu = []
        self.sushu = []
        self.panel = wx.Panel(self)
        size = wx.FlexGridSizer(0, 2, 10, 10)
        ShuStaticText = wx.StaticText(self.panel, -1, "Shu")
        ShuCtrlText = wx.TextCtrl(self.panel, -1,)


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
