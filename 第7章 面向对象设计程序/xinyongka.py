class CreidtCard:


    def __init__(self,number,password = 123456):
        self.number = number
        self.password = password
        if self.password == None:
            print('信用卡{}的默认密码为{}'.format(self.number,self.password))
        else:
            print('重置信用卡{}的密码为{}'.format(self.number,self.password))

newcard1 = CreidtCard('4013735633800642')

# print('信用卡'+newcard1.number+'的默认密码为'+str(newcard1.password))
# print('信用卡{}的默认密码为{}'.format(newcard1.number,newcard1.password))
# newcard2 = CreidtCard('4013735633800642','168779')
# print('重置信用卡'+newcard2.number+'的默认密码为'+str(newcard2.password))
