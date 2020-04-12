import requests
import json

cookie ={"_jc_save_fromDate":"2020-04-12",
         "_jc_save_fromStation":"BJP",
         "_jc_save_toDate":"2020-04-12",
         "_jc_save_toStation":"HHC",
         "_jc_save_wfdc_flag":"dc",
         "BIGipServerotn":"1406730506.50210.0000",
         "BIGipServerpassport":"887619850.50215.0000",
         "JSESSIONID":"D1E2416EDCAB23E19E20567FCCFFC0B9",
         "RAIL_DEVICEID":"opTBeHb-47xrAdLMtEfMtSfbVE0m2O-_-axF7HXF_7NLozzmOFAovsWBfqMDuRy8IJN_A8e3iUHzn2VgBaStggZr68H2r1LspErz0KmSkNC0X7fTax4BxD2sBmtt3PATOxDCLTv0Ylu92gbMaU5hwVC_x3Rbfnuh",
         "RAIL_EXPIRATION":"1586830351612",
         "route":"9036359bb8a8a461c164a04f8f50b252"}
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-04-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=HHC&purpose_codes=ADULT'
response = requests.get(url,cookies=cookie)
dictleftTicket = response.json()
httpstatus = dictleftTicket["httpstatus"]
result = dictleftTicket['data']['result']
print(httpstatus)
print(result)