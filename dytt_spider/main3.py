#coding=utf-8

import requests
from lxml import etree

BASE_URL = "https://www.dytt8.net"
HEADERS = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQB'
    'rowser/10.5.3805.400'
}
PROXY ={"http":"183.166.111.180:9999"}

#1.解析列表
def get_details(url):
    resp = requests.get(url,headers=HEADERS)
    text=resp.content.decode('gbk','ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan'//a/href")
    detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls

#1.获取列表页
def get_details_list():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,8):
        url=base_url.format(x)
        detail_urls = get_details(url)
        for detail in detail_urls:
            print(detail)

def baidu():
    resp=requests.get("https://baidu.com/")
    print(resp.text)
    with open('baidu.html','w',encoding='utf-8') as fp:
         fp.write(resp.text)

def get_html():
    resp=requests.get("https://www.dytt8.net/html/gndy/dyzz/list_23_1.html",headers=HEADERS,proxies=PROXY)
    with open('dytt.html','w',encoding='utf-8') as fp:
        fp.write(resp.text)

if __name__=='__main__':
    #get_details_list()
    #baidu()
    get_html()