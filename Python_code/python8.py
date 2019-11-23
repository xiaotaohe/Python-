#coding=utf-8

from urllib import request
from urllib import parse
#爬取拉钩网信息

# url = 'https://www.lagou.com/jobs' \
#       '/list_python?labelWords=&fromSearch=true&suginput='
# # resp = request.urlopen(url)
# # print(resp.read())
#
# headers = {'User-Agent':''
#                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit'
#                         '/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 '
#                         'Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'}
# resp = request.Request(url,headers=headers)
# resp=request.urlopen(resp)
# print(resp.read())

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# resp = request.urlopen(url)
# print(resp.read())

data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
headers = {'User-Agent':''
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit'
                        '/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 '
                        'Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
           # 'Referer':
           #     'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
           #  'X-Anit-Forge-Code': 0
           }

resp = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp=request.urlopen(resp)
print(resp.read().decode('utf-8'))



