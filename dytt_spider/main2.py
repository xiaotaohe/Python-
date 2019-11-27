#coding=utf-8

from lxml import etree
import requests

# 先获取电影列表，在获取列表中的单个电影信息

BASE_URL = "https://www.dytt8.net/"
# url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
HEADERS = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQB'
    'rowser/10.5.3805.400'
}
# PROXY={'http':'117.30.113.206:9999'}

MOVIES = []

#解析列表页
def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    # 当遇到编码问题，入gbk....,可以使用 'ignore'忽略错误
    # print(response.content.decode('gbk','ignore'))
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # lambda等价于：
    # def abc(url):
    #   return BASE_URL+url
    # index = 0;
    # for detail_url in detail_urls:
    #   detail_url = abc(detail_url)
    #   detail_urls[index] = detail_url
    #   index += 1
    detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    resp = requests.get(url,headers=HEADERS)
    text = resp.content.decode('gbk','ignore')
    html = etree.HTML(text)
    #解析
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")
    for x in title:
        print(x)


#获取列表页并解析列表页及详情页
def spider():
    # 花括号先当与占一个坑
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    # 左闭右开1~7
    for x in range(1,8):
        url = base_url.format(x)
        #print(url)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            print(detail_url)
            # parse_detail_page(detail_url)
            # break
        # break

        #print(url)

if __name__ =='__main__':
    spider()