#单下划线的类属性，不能从模块中导入，但是可以通过实例调用
# class Swan:
#     '''天鹅类'''
#     _neck_sawn = '天鹅的脖子很长'
#     def __init__(self):
#         print('__init__():',Swan._neck_sawn)
#
#
# swan = Swan()
# print('直接访问：',swan._neck_sawn)

# 双下划线的私有类型的成员，只允许定义该方法的类本身进行访问，或通过类实例名._类名__xxx的方式调用

class Swan:
    '''天鹅类'''
    __neck_swan = '天鹅的脖子很长'
    def __init__(self):
        print('__init__():',Swan.__neck_swan)

swan = Swan()
print('加入类名：',swan._Swan__neck_swan)
print('直接访问：',swan.__neck_swan)




