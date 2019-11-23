#coding=utf-8

from urllib import request


#这段代码用来获取未使用代理的本机IP地址

# url='http://www.httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())


#这段代码使用了代理的
#使用opener去访问服务器

#1.使用ProxyHandler创建代理
handler = request.ProxyHandler(
    {'http':'117.69.201.202:9999'})
url='http://httpbin.org/ip'
#2.使用上面的Handler创建一个opener
opener =  request.build_opener(handler)
# req = request.Request(url)#用来添加头部信息，防止反爬虫检测
#3.使用opener获取url的资源
req = opener.open(url)
print(req.read())