#coding=utf-8

from lxml import etree
import requests

# 先获取电影列表，在获取列表中的单个电影信息

url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"

headers = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQB'
    'rowser/10.5.3805.400',
}
proxy={'http':'171.35.168.116:9999'}

response = requests.get(url,headers=headers,proxies=proxy)
# 当遇到编码问题，入gbk....,可以使用 'ignore'忽略错误
# print(response.content.decode('gbk','ignore'))
text = response.content.decode('gbk','ignore')
html = etree.HTML(text)
movies_href=html.xpath("//table[@class='tbspan']//a/@href")

for movie_href in movies_href:
    print(movie_href)