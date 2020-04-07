import  wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建TextCtrl类', size=(400,300))
        #  创建面板
        panel = wx.Panel(self)
        #  创建文本和密码输入框
        self.title = wx.StaticText(panel,label='请输入用户名和密码',pos=(140, 20))
        self.label_user = wx.StaticText(panel, label='用户名：', pos=(50, 50))
        self.text_user = wx.TextCtrl(panel,pos=(110, 50), size=(235,25),style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,pos=(50, 90), label='密    码：')
        self.text_password = wx.TextCtrl(panel,pos=(110, 90), size=(235 ,25), style=wx.TE_PASSWORD)
        #  创建“确定”和“取消”按钮,并绑定事件
        self.bt_confir = wx.Button(panel,label='确定',pos=(90,130))
        self.bt_confir.Bind(wx.EVT_BUTTON,self.onclickSubmit)
        self.bt_cancel = wx.Button(panel,label='取消',pos=(215,130))
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.onclickCancel)

    def onclickSubmit(self,event):
        '''单击确定按钮，执行方法'''
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        if username == '' or password == '':
            message = '用户名户密码不能为空'
        elif username == 'mr' and password == 'mrsoft':
            message = '登录成功'
        else:
            message = '用户名和密码不匹配'
        wx.MessageBox(message)

    def onclickCancel(self,event):
        '''  单击取消按钮，执行方法  '''
        self.text_user.SetValue('')
        self.text_password.SetValue('')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
