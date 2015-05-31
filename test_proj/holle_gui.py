import wx
import sys


class Frame(wx.Frame):
    def __init__(self, image, parent = None, id = -1, title = "Hello wxpython",
                 pos = wx.DefaultPosition,style = wx.DEFAULT_FRAME_STYLE^(wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX)):
        print "frame"
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.bmp = wx.StaticBitmap(self, bitmap = temp)
        panel = wx.Panel(self)
        button = wx.Button(panel, label = "close" )
        self.Bind(wx.EVT_BUTTON, self.Close(True), button)
        self.Bind(wx.EVT_CLOSE, self.Destroy())

class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect = False)
        print sys.stdout,"init"
    def OnInit(self):
        print  sys.stderr,"oninit"
        image1 = wx.Image("test.jpg", wx.BITMAP_TYPE_JPEG)
        id1 = wx.NewId()
        self.frame = Frame(image1, id = id1)
        print self.frame.GetId()
        image2 = wx.Image("test1.jpg",wx.BITMAP_TYPE_JPEG)
        id2 = wx.NewId()
        self.frame1 = Frame(image2, id = id2)
        print self.frame1.GetId()
        if self.frame.GetSize() > self.frame1.GetSize():
            self.frame.Show()
            self.frame1.Show()
        else:
            self.frame1.Show()
            self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    print "main"
    app = App()
    print "app"
    app.MainLoop()
    print "mainloop"


if __name__ == '__main__':
    main()

