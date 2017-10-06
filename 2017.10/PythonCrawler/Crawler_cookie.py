#coding=utf-8
#2017.10.6,Flash, catch edu website

#模拟登录并未实现，待后期修改实现

import urllib
import urllib2
import cookielib

filename= "cookiemi.txt"

#声明一个MozillaCookieJar 对象实例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({"username":"97697551@qq.com","password":"SX20121212XT"})
loginurl = "https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"
#模拟登录，并把cookie保存到变量
headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0",
		"Referer":"account.xiaomi.com",
		"Host":"account.xiaomi.com",
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accepet-Encoding":"gzip, deflate, br",
		"Connection":"Keep-alive",
		"Upgrade-Insecure-Requests":"1"		
		}
request = urllib2.Request(loginurl, postdata, headers)

result = opener.open(request)

#保存到 cookiexjtu.txt中
cookie.save(ignore_discard = True,ignore_expires = True)

#利用cookie请求访问另一个网址
gradeurl="https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fbbs.xiaomi.cn%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fbbs.xiaomi.cn%252F%26sign%3DM2E4MTg3MzE3MGJmZGFiMTc0MTE5NmNjZTAyYWNmMDZhNTEwOTU2NQ%2C%2C&sid=new_bbs_xiaomi_cn&_locale=zh_CN"
request2 = urllib2.Request(gradeurl, postdata, headers)
#请求访问成绩查询网址
result = opener.open(request2)
print result.read()
