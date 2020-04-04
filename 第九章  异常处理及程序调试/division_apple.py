def divison():
    '''功能：分苹果'''

    print('\n'+'='*15+'分苹果了'+'='*15)
    apple = int(input('请输入苹果的个数：'))
    children = int(input('请输入来了几个小朋友：'))
    result = apple//children
    remain = apple - result*children
    if remain > 0 :
        print('{}个苹果，平均分给{}个小朋友，每人分{}个，剩下{}个。'.format(apple,children,result,remain))
    else:
        print('{}个苹果，平均分给{}个小朋友，每人分{}个。'.format(apple,children,result))

if __name__ == '__main__':
    divison()
