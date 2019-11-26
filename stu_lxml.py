#coding=utf-8

from lxml import etree
import requests

# url = 'https://www.lagou.com/'
# proxy={'http':'171.35.168.116:9999'}
# resp = requests.get(url,proxies=proxy)
# print(resp.cookies)
# cookie = resp.cookies
# print(type(cookie))
# print(cookie)
# data={'first': 'true',
# 'pn': 1,
# 'kd': 'python'}
#
# resp = requests.post(url,proxies=proxy,data=data)
# with open('position.html','w',encoding='utf-8') as fp:
#     fp.write(resp.content.decode())


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser=parser)

# 获取div标签
# divs = html.xpath('//div')
# for div in divs:
#     print(etree.tostring(div,encoding='utf-8').decode('utf-8'))

# 获取第2个div
# div = html.xpath('//div[2]')[0]
# print(etree.tostring(div,encoding='utf-8').decode('utf-8'))

# 获取所有class等于search-content的div对象
divs = html.xpath("//div[@class='search-content']")
for div in divs:
    print(etree.tostring(div,encoding='utf-8').decode('utf-8'))
