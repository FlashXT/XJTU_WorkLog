#coding=utf-8
#2017.10.6,Flash,cookielib

import urllib2
import cookielib

#����һ��cookieJar����ʵ��������cookie
cookie = cookielib.CookieJar()
#����urllib2���HTTPCookieProcessor����������cookie������
handler = urllib2.HTTPCookieProcessor(cookie)
#ͨ��handler������opener
opener = urllib2.build_opener(handler)
#�˴���open����ͬurllib2��urlopen������Ҳ���Դ���request
response = opener.open("http://www.baidu.com")
for item in cookie:
	print "Name = " +item.name
	print "Value = " + item.value
