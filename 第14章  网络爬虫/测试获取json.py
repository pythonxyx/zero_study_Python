import requests
import urllib
import json


"""获取data"""
def getData(url):
    data = ''
    while 1:
        try:
            headers = {'User-Agent':"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-04-11&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=HHC&purpose_codes=ADULT"}
            req = urllib.request.Request(url=url,headers=headers)
            data = urllib.request.urlopen(req).read().decode('utf-8')
            if data.startswith(u'\ufeff'):
                data = data.encode('utf8')[3:].decode('utf-8')
            break
        except:
            print('获取data失败，继续获取……')
            continue
    return data

"""获取result"""
def resolveData():
    #  查询链接
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-04-11&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=HHC&purpose_codes=ADULT'
    while 1:
        try:
            data = getData(url)
            lists = json.loads(data)["data"]["result"]
            break
        except:
            print('2获取失败，继续中……')
            continue  #获取失败时则重新获取
    for item in lists:
        print(item)

resolveData()
