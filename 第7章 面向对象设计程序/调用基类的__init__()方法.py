class Fruit:
    def __init__(self,color = '绿色'):
        self.color = color
    def harvest(self):
        print('水果原来是：'+self.color+'的！')

class Apple(Fruit):
    def __init__(self):
        super().__init__()  # 调用fruit基类的__init__方法进行初始化，否则调用harvest时会报错
        print('我是苹果')


apple = Apple()
apple.harvest()
