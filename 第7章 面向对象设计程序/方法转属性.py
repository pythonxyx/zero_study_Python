class Boy:

    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
    @property
    def bmi(self):
        return self.height*self.weight


xiaoming = Boy('小明',80,170)
print(xiaoming.name)
print(xiaoming.weight)
print(xiaoming.bmi)  # 方法转属性后，调用时，不用加括号