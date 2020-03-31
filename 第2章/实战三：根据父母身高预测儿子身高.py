Dad_height = float(input('请输入父亲的身高：'))
Mom_height = float(input('请输入母亲的身高：'))
Kid_height = (Dad_height+Mom_height)*0.54
print('预测孩子的身高为：'+str(Kid_height))  #第一种表达方式
print('预测孩子的身高为：%.2f' % Kid_height)  #第二种表达方式
print('预测孩子的身高为：{}'.format(Kid_height))  #第三种表达方式