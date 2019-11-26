#coding=utf-8

import requests
from lxml import etree

# 1.将目标网站上的页面抓取下来
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',
    'Referer':'https://movie.douban.com'
}
url='https://movie.douban.com/cinema/nowplaying/xian/'
response =requests.get(url,headers=headers)
# print(response.text)
# response.text：返回的是一个经过解码后的字符串，时str（unicode）类型
# response.content：返回的是一个原生的字符串，就是从网页上抓取下来的，
# 没经过处理的字符串，是bytes类型
text = response.text

# 2.将抓取下来的数据根据一定的规则进行提取
html=etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies =[]
for li in lis:
    title = li.xpath("@data-title")[0]
    score =li.xpath("@data-score")[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    release = li.xpath('@data-release')[0]
    thumbnail = li.xpath('.//img/@src')[0]
    href = li.xpath('.//a/@href')[0]
    movie = {
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'release':release,
        'thumbnail':thumbnail,
        'href':href
    }
    movies.append(movie)
print(movies)


# print(ul)
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
