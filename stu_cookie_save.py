#encoding=utf-8

from urllib import request
from http.cookiejar import CookieJar
from urllib import parse
from http.cookiejar import MozillaCookieJar

# 1.创建cookiejar对象
cookiejar = MozillaCookieJar('cookie.txt')
# 2.加载一些已经被忽略（即窗口已关闭）的cookie信息
cookiejar.load(ignore_discard=True)
# 3.通过cookiejar对象创建handler对象
handler = request.HTTPCookieProcessor(cookiejar)
for cookie in cookiejar:
   print(cookie)
opener = request.build_opener(handler)
headers = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; '
    'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/75.0.3770.100 Safari/537.36'
}

url = 'http://httpbin.org/cookies/set?course=splid'
resp = opener.open('http://www.baidu.com/')
req = request.Request(url,headers=headers)
resp = opener.open(req)

cookiejar.save(ignore_discard=True)
