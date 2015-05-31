import wx


class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "button_wxpython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)
        button1 = wx.Button(panel, label = "b1") #sizer
        sizer.Add(button1)
        button2 = wx.Button(panel, label = "b2")
        sizer.Add(button2)
        self.sizer = sizer
        self.panel = panel

        self.Bind(wx.EVT_BUTTON, self.OnButton1Click, button2)
        button1.Bind(wx.EVT_BUTTON, self.OnButtonClick)

        self.Bind(wx.EVT_BUTTON, self.OnButton2Click, button1)
        button2.Bind(wx.EVT_BUTTON, self.OnButtonClick)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #sizer wxBoxSizer

    def OnButton1Click(self, event):
        print "button1 click"

    def OnButton2Click(self, event):
        print "button2 click"

    def OnButtonClick(self,event):
        print "button"
        event.Skip()
        id = event.GetId()
        win = self.FindWindowById(id)
        print win.GetLabel()

        button = wx.Button(self.panel, label = "b1") #sizer
        button.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.sizer.Add(button)
        self.panel.Layout()
        self.Refresh()


    def OnCloseWindow(self, event):
        print "window"
        self.Destroy()

class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect = False)

    def OnInit(self):
        self.frame = Frame(parent = None, id = -1)
        self.frame.Show()
        return True

def main():
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()

