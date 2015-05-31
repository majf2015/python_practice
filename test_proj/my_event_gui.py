import  wx


class MyEvevt(wx.CommandEvent):
    def __init__(self, eventtype, id):
        wx.CommandEvent.__init__(self, eventtype, id)

myEVT_BUTTON_CLICK = wx.NewEventType()
EVT_BUTTON_CLICK = wx.PyEventBinder(myEVT_BUTTON_CLICK,1)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1)
        panel = wx.Panel(self)
        #111111, c,d,e,f
        sizer = self.CreateButton(panel,4, 4)
        panel.SetSizer(sizer)
        centext = wx.StaticText(panel, -1, "dear my love\nyou are my one and only\n i seem to fall in love with you",
            (-1, -1), (200,100), wx.ALIGN_CENTER)
        centext.SetForegroundColour("blue")
        centext.SetBackgroundColour("yellow")
        sizer.Add(centext)

        sizer.Layout()
    def ClearButton(self):
        #t
        #33333333
        pass

    def CreateButton(self, parent, row, col):
        # 4444444
        sizer = wx.BoxSizer(wx.VERTICAL)
        n = 0
        while n < row:
            s = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(s, 1, wx.ALIGN_CENTER)
            n = n +1
            m = 0
            while m < col:
                button = wx.Button(parent,label = 'BUTTON')
                button.Bind(EVT_BUTTON_CLICK, self.MyButtonClick, button)
                button.Bind(wx.EVT_BUTTON, self.ButtonClick, button)
                s.Add(button, 1)
                m = m+1
        return sizer

    def ButtonClick(self, event):
        #222222, file or folder?
        eve = MyEvevt(myEVT_BUTTON_CLICK,event.GetId())
        button = self.FindWindowById(event.GetId())
        a = button.GetEventHandler()
        a.ProcessEvent(eve)

    def MyButtonClick(self, event):
        id = event.GetId()
        button = self.FindWindowById(id)
        print button.GetLabel()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()