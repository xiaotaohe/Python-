#coding=utf-8

import requests

#一般请求
# resp = requests.get('http://httpbin.org/ip')
# print(resp.content.decode('utf-8'))

# 任务一：使用代理

# proxy = {'http':'171.35.168.116:9999'}
# # resp = requests.get('http://www.httpbin.org/ip',proxies=proxy)
# # print(resp.text)

# 任务二：获取Cookie信息
# proxy = {'http':'171.35.168.116:9999'}
# resp = requests.get('http://www.baidu.com/')
# print(resp.cookies.get_dict())

# 任务三：session
headers={'User-Agent':
			'Mozilla/5.0(WindowsNT10.0;WOW64)'
			'AppleWebKit/537.36(KHTML,likeGecko)'
			'Chrome/70.0.3538.25Safari/537.36Core/1.70.3730.400'
			'QQBrowser/10.5.3805.400'}
data={'email':"130229",
			'password':'1234'}
Login_url='http://www.renren.com/PLogin.do'


session = requests.Session()
session.post(Login_url,data=data,headers=headers)
resp=session.get('http://www.renren.com/880151247/profile')
with open('renren_dapeng.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)

