
phone_time = ['0分钟','50分钟','100分钟','300分钟']
index = list(range(1,6))
phone_time_dic = dict(zip(index,phone_time))

phone_liuliang = ['0M','500M','1G','5G','不限量']
phone_liuliang_dic = dict(zip(index,phone_liuliang))

phone_txt = ['0条','50条','100条']
phone_txt_dic = dict(zip(index,phone_txt))

print('定制自己的手机套餐：\n')
print('A.请设置通话时长：')
for x,y in phone_time_dic.items():
    print(str(x)+'.'+y)
phone_time_select = int(input('请输入选择的通话时长编号:'))

print('B.请设置流量包：')
for x,y in phone_liuliang_dic.items():
    print(str(x)+'.'+y)
phone_liuliang_select = int(input('请输入选择的流量包编号：'))

print('C.请设置短信条数：')
for x,y in phone_txt_dic.items():
    print(str(x)+'.'+y)
phone_txt_select = int(input('请输入选择的短信条数编号：'))

print('您的手机套餐定制成功：免费通话时长为{}/月，流量为{}/月，短信条数为{}/月'
      .format(phone_time_dic[phone_time_select],phone_liuliang_dic[phone_liuliang_select],phone_txt_dic[phone_txt_select]))

# 可利用下面的函数来输出通话时间、流量和短信的字典
# def shuchudic(n={}):
#     for x,y in n.items():
#         print(str(x)+'.'+y)
# shuchudic(phone_time_dic)
# shuchudic(phone_txt_dic)
