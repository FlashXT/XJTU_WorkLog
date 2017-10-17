#coding=utf-8
#2017.10.6,Flash,cookielib

import urllib2
import cookielib

filename="cookiebd.txt"
#声明一个cookieJar对象实例来保存cookie
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open("http://www.baidu.com")
#for item in cookie:
#	print "Name = " +item.name
#	print "Value = " + item.value
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
print "OK !"
