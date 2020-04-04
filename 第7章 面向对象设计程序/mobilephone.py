class MobilePhone:

    def moren(self):
        print('智能手机的默认语言为英语')

    def change(self,newlaguge):
        print('将智能手机的默认语言设置为'+newlaguge)


aphone = MobilePhone()
aphone.moren()
aphone.change('中文')
