def divison():
    '''功能：分苹果'''

    print('\n'+'='*15+'分苹果了'+'='*15)
    apple = int(input('请输入苹果的个数：'))
    children = int(input('请输入来了几个小朋友：'))
    assert not apple < children,'大哥，苹果不够分啊'  # 如果表达式为假时，才输出后面的错误信息！！！！
    if children == 1:
        result = apple - 1
    else:
        result = apple // children
    remain = apple - result*children
    if remain > 0 :
        print('{}个苹果，分给{}个小朋友，每人分{}个，剩下{}个。'.format(apple,children,result,remain))
    else:
        print('{}个苹果，平均分给{}个小朋友，每人分{}个。'.format(apple,children,result))

if __name__ == '__main__':
    while True:
        try:
            divison()
        except ZeroDivisionError:
            print('\n出错了，苹果不能被0个小朋友分！！')
        except ValueError as err:
            print('输入错误：'+str(err))
        except AssertionError as err:
            print('\n输入有误'+str(err))
        else:
            print('苹果顺利分完了~~~~')
        finally:
            print('进行了一次苹果操作！！')

        choose = input('您是否需要继续查询（是/否）：')
        if choose == '否':
            break
        else:
            pass


