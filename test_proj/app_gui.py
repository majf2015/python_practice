import wx


a = wx.App()

frame1 = wx.Frame(None, -1, "myapp1", size = (200, 400))

frame2 = wx.Frame(frame1, -1, "myapp2", size = (300, 500))

frame3 = wx.Frame(frame2, -1, "myapp3", size = (400, 600))
frame3.Show(True)
frame2.Show(True)
frame1.Show(True)

a.SetTopWindow(frame1)
a.MainLoop()
