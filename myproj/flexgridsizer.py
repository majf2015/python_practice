import wx
import os


class FileFrame(wx.Frame):
    def __init__(self):
        self.dir = {1: 'C:', 2: 'D:', 3: 'E:', 4: 'F:'}
        self.path = ''
        wx.Frame.__init__(self, None, -1, "File Manager")
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel = wx.ScrolledWindow(self, -1)
        self.panel.SetScrollbars(100, 100, 60000, 60000, 200, 200)
        self.main_sizer.Add(self.panel, 1, wx.EXPAND)
        self.top_sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer1 = wx.FlexGridSizer(0, 4, 10, 10)
        self.CreateButton()
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        button = wx.Button(self.panel, -1, 'Up')
        button.Bind(wx.EVT_BUTTON, self.UpClick, button)
        self.sizer2.Add(button, 0, wx.ALIGN_CENTER)
        self.top_sizer.Add(self.sizer1, 1, wx.EXPAND)
        self.top_sizer.Add(self.sizer2, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.top_sizer)
        self.SetSizer(self.main_sizer)
        self.Layout()

    def CreateButton(self):
        for k, v in self.dir.iteritems():
            button = wx.Button(self.panel, k, v)
            button.Bind(wx.EVT_BUTTON, self.ButtonClick, button)
            self.sizer1.Add(button)

    def ButtonClick(self, event):
        id = event.GetId()
        win = self.FindWindowById(id)
        if self.path == '':
            self.path = win.Label + '/'
            #self.path = os.path.join(self.path, win.Label)
        else:
            self.path = os.path.join(self.path, win.Label)

        self.ClearSizer(self.sizer1)
        #self.top_sizer.Detach(self.sizer1)

        if os.path.isfile(self.path):
            self.PrintFile()
        else:
            self.CreateDir()

            self.CreateButton()
            #self.top_sizer.Insert(self.sizer1, )
            #self.top_sizer.Add(self.sizer1, 1, wx.EXPAND)
            self.Layout()

    def UpClick(self, event):
        if self.path == '':
            message = wx.MessageBox(parent = self, message = "this is the top path", style = wx.OK)
            return

        p = os.path.dirname(self.path)
        if self.path == p:
            self.path = ''
            self.dir = {1: 'C:', 2: 'D:', 3: 'E:', 4: 'F:'}
        else:
            self.path = p
            self.CreateDir()

        self.ClearSizer(self.sizer1)
        #self.top_sizer.Detach(self.sizer1)
        self.CreateButton()
        #self.top_sizer.Add(self.sizer1, 1, wx.EXPAND)
        self.Layout()

    def PrintFile(self):
        with open(self.path, 'r') as f:
            text = wx.StaticText(self.panel, -1, f.read())
            self.sizer1.Add(text)
            self.Layout()

    def ClearSizer(self, sizer):
        for i in sizer.GetChildren():
            if i.IsWindow():
                i.GetWindow().Destroy()
            elif i.IsSizer():
                self.ClearSizer(i.GetSizer())
        sizer.Clear()

    def CreateDir(self):
        self.dir.clear()
        lis = os.listdir(self.path)
        n = 1
        for i in lis:
            self.dir[n] = i
            n += 1

if __name__ =="__main__":
    app = wx.App()
    frame = FileFrame()
    frame.Show()
    app.MainLoop()