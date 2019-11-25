#coding=utf-8

import requests
from urllib import  request

#response=requests.get("http://ww.baidu.com/")
# print(type(response.text))
#print(response.text)

# print(type(response.content))
# print(response.content.decode('utf-8'))
#
# print(response.url)
# print(response.encoding)
# print(response.status_code)

# 1.requests.get()
# params ={
#     'wd':'中国'}
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'
#              ' AppleWebKit/537.36 (KHTML, like Gecko) '
#              'Chrome/70.0.3538.25 Safari/537.36 Core/'
#              '1.70.3730.400 QQBrowser/10.5.3805.400',
#              #'Referer': 'https://www.baidu.com/'
# }
# response=requests.get('http://www.sougou.com/s'
#                       ,params=params,headers=headers)
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))
# print(response.url)


#2.post


data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'
             ' AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/70.0.3538.25 Safari/537.36 Core/'
             '1.70.3730.400 QQBrowser/10.5.3805.400',
             #'Referer': 'https://www.baidu.com/'
'Referer':' https://www.lagou.com/jobs/list_python?'
          'labelWords=&fromSearch=true&suginput=',
'Cookie':'_ga=GA1.2.1726135074.1574500691; user_trace_token=20191123171808-2a187beb-0dd2-11ea-a881-525400f775ce; LGUID=20191123171808-2a187f10-0dd2-11ea-a881-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e978ece131c4-0487f9155039f-34564b7b-1049088-16e978ece14578%22%2C%22%24device_id%22%3A%2216e978ece131c4-0487f9155039f-34564b7b-1049088-16e978ece14578%22%7D; _gid=GA1.2.2081612273.1574596040; LGSID=20191124194718-2ac32f8f-0eb0-11ea-a8d0-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574596738,1574597358,1574597369,1574597635; gate_login_token=711c411b2e490826f4694211b21fc1981057a2aa858ef96368b0d2a865135642; _putrc=B6D58DC7F2D914EC123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B78230; privacyPolicyPopup=false; _gat=1; X_HTTP_TOKEN=43e437c8e1b2011283089547515a30bc57e9819f12; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574598042; LGRID=20191124202040-d400fe3d-0eb4-11ea-a677-5254005c3644'
}
#1.使用代理
# handler=request.ProxyHandler({'http':'49.89.221.119:9999'})
# opener=request.build_opener(handler)
#
# req = opener.open('http://httpbin.org/ip')
# print(req.read())
response = requests.get('http://www.httpbin.org/ip')
print(response.text)
# response = requests.post('https://www.lagou.com/jobs'
#                         '/positionAjax.json?needAddtionalResult=false',
#                         data=data)
response = requests.get('http://www.lagou.com/')
print(type(response.text))
print(response.text)