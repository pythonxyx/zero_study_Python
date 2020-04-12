from get_stations import *


data = []
type_data = []


def query(date,from_station,to_station):
    data.clear()
    type_data.clear()
    #  查询请求地址
    cookie = {"_jc_save_fromDate": "",
              "_jc_save_fromStation": "",
              "_jc_save_toDate": "",
              "_jc_save_toStation": "",
              "_jc_save_wfdc_flag": "dc",
              "BIGipServerotn": "1406730506.50210.0000",
              "BIGipServerpassport": "887619850.50215.0000",
              "JSESSIONID": "D1E2416EDCAB23E19E20567FCCFFC0B9",
              "RAIL_DEVICEID": "opTBeHb-47xrAdLMtEfMtSfbVE0m2O-_-axF7HXF_7NLozzmOFAovsWBfqMDuRy8IJN_A8e3iUHzn2VgBaStggZr68H2r1LspErz0KmSkNC0X7fTax4BxD2sBmtt3PATOxDCLTv0Ylu92gbMaU5hwVC_x3Rbfnuh",
              "RAIL_EXPIRATION": "1586830351612",
              "route": "9036359bb8a8a461c164a04f8f50b252"}
    stations = eval(read())
    cookie["_jc_save_fromDate"]=date
    cookie["_jc_save_fromStation"]=stations[from_station]
    cookie["_jc_save_toDate"]=date
    cookie["_jc_save_toStation"]=stations[to_station]
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}' \
          '&leftTicketDTO.from_station={}' \
          '&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,stations[from_station],stations[to_station])
    #  发送查询请求
    response = requests.get(url,cookies=cookie)
    #  将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    #  判断车站文件是否存在
    if isStations() == True:
        stations = eval(read())
        if len(result) != 0:
            for i in result:
                #  分割数据并添加到列表中
                tmp_list = i.split('|')
                #  因为查询结果中出发站和到达站为站名的缩写字母，
                #  所以需要在车站库中找到对应的车站名称
                from_station =\
                list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station =\
                list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                #  创建座位数组，由于返回的座位数据中含有空（即""），所以将空改成"--"
                seat = [tmp_list[3],from_station,to_station,tmp_list[8],
                        tmp_list[9],tmp_list[10],tmp_list[32],tmp_list[31],
                        tmp_list[30],tmp_list[21],tmp_list[23],tmp_list[33],
                        tmp_list[28],tmp_list[24],tmp_list[29],tmp_list[26],]
                newSeat = []
                for s in seat:
                    if s == "":
                        s = "--"
                    elif s == "24:00":
                        s = "---"
                    elif s == "99:59":
                        s = "---"
                    else:
                        s = s
                    newSeat.append(s)
                data.append(newSeat)
    return data

if __name__ == "__main__":
    query("2020-04-13","北京","上海")
    for x,y in enumerate(data):
        print(x,y)



