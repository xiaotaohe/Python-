#coding=utf-8

from urllib import parse

url='https://www.bilibili.com/video/av44518113/?p=7'
#url='https://www.bilibili.com/video/av44518113/;hello?p=7'  params处于 ; 与 ？之间
result = parse.urlparse(url)
print(parse.urlparse(url))
print(parse.urlsplit(url))  #split没有params字段
print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)