import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = '创建StaticText类',
                          pos=(100,100),size=(600,400))
        panel = wx.Panel(self)
        title = wx.StaticText(panel,label='Python之禅——Tim Peters',pos=(100,20))
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title.SetFont(font)
        wx.StaticText(panel,label='优美胜于丑陋',pos=(50,50))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

