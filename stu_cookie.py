#coding=utf-8

# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request

#1.不使用cookie去请求大鹏的主页
# dapeng_url = "http://www.renren.com/880151247/profile"
# headers = {'User-Agent':
#                'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                'AppleWebKit/537.36 (KHTML, like Gecko) '
#                'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 '
#                'QQBrowser/10.5.3805.400'}
# req = request.Request(url=dapeng_url,headers=headers)
# resp = request.urlopen((req))
# #print(resp.read().decode('utf-8'))
# with open('renren.html','w') as fp:
#     #write函数必须写入一个str的数据类型
#     #resp.read()读出来的是一个bytes数据类型
#     #bytes->decode->str
#     #str->encode->bytes
#     fp.write(resp.read().decode('utf-8'))
#此时得到数据为登录页面


#2.设置cookie信息，通过抓包获取cookie信息

# dapeng_url = "http://www.renren.com/880151247/profile"
# headers = {'User-Agent':
#                'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                'AppleWebKit/537.36 (KHTML, like Gecko) '
#                'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 '
#                'QQBrowser/10.5.3805.400',
#            'Cookie':'anonymid=k3cerhg1y5vgbw;'
#                     ' depovince=GW; _r01_=1;'
#                     ' JSESSIONID=abcyw4sbW4JAx-z5dvB6w;'
#                     ' ick_login=0e25c00d-3a3b-4932-ba55-51180a00bf96; '
#                     'loginfrom=null; wp_fold=0; '
#                     't=b05e0cd106977db3ec98c79c18f5f36b7;'
#                     ' societyguester=b05e0cd106977db3ec98c79c18f5f36b7;'
#                     ' id=972938717; xnsid=64a53a99; '
#                     'jebecookies=d8e5607e-6d11-485a-9027-1ade8f351142|||||; '
#                     'ver=7.0'}
# req = request.Request(url=dapeng_url,headers=headers)
# resp = request.urlopen((req))
# #print(resp.read().decode('utf-8'))
# with open('renren.html','w',encoding='utf-8') as fp:
#     #write函数必须写入一个str的数据类型
#     #resp.read()读出来的是一个bytes数据类型
#     #bytes->decode->str
#     #str->encode->bytes
#     fp.write(resp.read().decode('utf-8'))


#3.利用http.cookiejar和request.HTTPCookieProcessor登录人人网
from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; WOW64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 '
               'QQBrowser/10.5.3805.400'}

def get_opener():
    #1. 登录
    #1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    #1.2 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    #1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener;

def Login_renren(opener):
    #1.4 使用opener发送登录请求（人人网的邮箱和密码)
    data = {'email':"13022988230",
            'password':'taochao19970123'}
    Login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(Login_url,data=parse.urlencode(\
        data).encode('utf-8'),headers=headers)
    opener.open(req)

def visit_profile(opener):
    #2.访问个人主页
    dapeng_url = "http://www.renren.com/880151247/profile"
    # 获取个人主页的页面的时候，不要新建一个opener
    # 而应该使用之前的那个opener，因为之前的那个opener已经包含了
    # 登陆所需要的cookie信息
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(dapeng_url)
    with open('renren.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    Login_renren(opener)
    visit_profile(opener)

