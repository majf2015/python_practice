import wx


class Print_Label_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel = wx.Panel(self)
        self.panel.SetSizer(self.sizer)
        my_name = wx.Button(self.panel, label = 'my_name')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, my_name)
        self.sizer.Add(my_name)
        my_age = wx.Button(self.panel, label = 'my_age')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, my_age)
        self.sizer.Add(my_age)
        my_address = wx.Button(self.panel, label = 'my_address')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, my_address)
        self.sizer.Add(my_address)

    def ButtonClick(self, event):
        id = event.GetId()
        button = self.FindWindowById(id)
        label = button.GetLabel()
        dialog = wx.MessageDialog(None, "xxx", "button_name", wx.OK | wx.CANCEL |wx.ICON_QUESTION)
        dialog.ShowModal()
        print wx.ID_YES
        print wx.ID_NO
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = Print_Label_Frame()
    frame.Show()
    app.MainLoop()
