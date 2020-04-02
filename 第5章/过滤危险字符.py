def filterchar(txt):

    '''过滤掉一些危险的字符
    '''
    import re
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
    sub = re.sub(pattern,'***',txt)
    print(sub)


about = '我是一名程序员，喜欢看黑客方面的图书，想研究下Trojan！'
filterchar(about)

# import re
# pattern = r'(黑客|Trojan)'
# new = re.findall(pattern,about)
# print(new)



