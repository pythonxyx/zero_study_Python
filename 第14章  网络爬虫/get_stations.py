import requests
import os
import re

def getStation():
    #  发送请求获取所有车站名称，通过输入的站名转换为查询地址的参数
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/' \
          'station_name.js?station_version=1.9142'
    response = requests.get(url, verify=True)
    #  获取需要的车站名称
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
    stations = dict((stations))
    stations = str(stations)
    write(stations)


def write(stations):
    file = open('stations.txt',"w",encoding='utf_8_sig')
    file.write(stations)
    file.close()


def read():
    file = open('stations.txt','r',encoding='utf_8_sig')
    data = file.readline()
    file.close()
    return data


def isStations():
    isStations = os.path.exists('stations.txt')
    return isStations


if __name__ == '__main__':
    getStation()
