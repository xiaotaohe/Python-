# coding=utf-8

import urllib.parse
import time
from pip._internal.cli.cmdoptions import platform

def clear():
    #该函数用于清屏
    print(u'内容比较多，显式三秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if OS == u'Windows':
       OS.system('cls')
    else:
        OS.system(clear())
def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url,timeout=3)
    except urllib.request.URLError:
        print(u"网络地址错误")
        exit()
    with open('./baidu.txt','w') as fp:
        fp.write(response.read().decode())
    print(u"获取url信息，response.geturl()\n:%s"%response.geturl())
    print(u"获取返回代码，response.getcode()\n:%s"%response.getcode())
    print(u"获取返回信息，response.info()\n:%s"%response.info())
    print(u"获取网页内容已存入当前目录的baidu.txt中，请自行查看")
if __name__ == '__main__':
    linkBaidu()