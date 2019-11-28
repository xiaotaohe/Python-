#coding=utf-8

import requests
from lxml import etree

HEADERS={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
'Cookie': 'UM_distinctid=16ea71044a80-014afcab5986f9-34564b7b-100200-16ea71044ac17c'
}

# PROXY={'http':"117.69.200.188:9999"}
BASE_URL = "https://ygdy8.com"

#1.生成多个列表页
def get_liet_pages():
    url = "https://ygdy8.com/html/gndy/dyzz/list_23_{}.html"
    url_pages = []
    for x in range(1,2):
        page_url = url.format(x)
        url_pages.append(page_url)
    return url_pages

#2.请求单个列表页，获取每个电影的url信息
def get_movie_urls(url):
    resp = requests.get(url,headers=HEADERS)
    text = resp.content.decode('gbk','ignore')
    html = etree.HTML(text)
    urls=html.xpath("//div[@class='co_content8']//table//a/@href")
    # 在链接前面加上base_url
    urls = map(lambda url:BASE_URL+url,urls)
    return urls

MOVIES = []
#3.请求并分析每个电影
def parse_movie(url):
    movie = {}
    resp = requests.get(url,headers=HEADERS)
    text = resp.content.decode('gbk','ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title
    cover = html.xpath("//img/@src")
    movie['cover'] = cover
    zoom = html.xpath("//div[@id='Zoom']//span[@style='FONT-SIZE: 12px']")[0]
    # 解析Zoom下的每个电影的详情
    infos = zoom.xpath("//text()")
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print("="*40)
        if info.startswith("◎译　　名"):
            info.replace("◎译　　名","").strip()
            movie['e_name'] = info
        elif info.startswith("◎片　　名"):
            info.replace("◎片　　名","").strip()
            movie['name'] = info
        elif info.startswith("◎年　　代"):
            info.replace("◎年　　代","").strip()
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info.replace("◎产　　地","").strip()
            movie['placename'] = info
        elif info.startswith("◎豆瓣评分"):
            info.replace("◎豆瓣评分","").strip()
            movie['core'] = info
        elif info.startswith("◎片　　长"):
            info.replace("◎片　　长","").strip()
            movie['time'] = info
        elif info.startswith("◎导　　演"):
            info.replace("◎导　　演","").strip()
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info.replace("◎主　　演","").strip()
            actors = info
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if(actor.startswith("◎")):
                    break
                actors += actor+" "
            movie['actor'] = actors
                # print (actor)
        elif info.startswith("◎简　　介 "):
            info.replace("◎简　　介 ","").strip()
            movie['intro'] = info
            for x in range(index+1,len(infos)):
                intro = infos[x].strip()
                if(intro.startswith("◎")):
                    break
                movie['intro'] = intro
                # print(intro)
        Download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
        movie['Download_url'] = Download_url
        #print(Download_url)
    return movie


#4.获取每个电影海报并提取信息
def get_movies():
    url_pages = get_liet_pages()
    for url in url_pages:
        #1.请求单表，获取每个电影的url
        movie_urls=get_movie_urls(url)
        #2.得到每个电影的url，请求每个电影url并获取每个电影的信息
        for url in movie_urls:
            movie = parse_movie(url)
            MOVIES.append(movie)
        for movie in MOVIES:
            print(movie)
        print(len(MOVIES))
    # 打印各个电影详情页的链接
    # for url in movie_urls:
    #     print(url)



if __name__ == "__main__":
    get_movies()