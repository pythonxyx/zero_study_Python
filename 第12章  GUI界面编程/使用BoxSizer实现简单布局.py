import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'用户登录',size=(400,300))

        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label='请输入用户名和密码')

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.Bottom|wx.Top|wx.ALIGN_CENTER,border=15)
        panel.SetSizer(vsizer)
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
