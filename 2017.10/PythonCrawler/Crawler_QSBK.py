#coding=utf-8
#2017.10.5,0:00,Falsh,ÅÀ³æôÜÊÂ°Ù¿Æ
import urllib
import urllib2

page = 1
url="https://www.qiushibaike.com/hot"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={"User-Agent":user_agent}
try:
	 request = urllib2.Request(url)
	 response = urllib2.urlopen(request)
	 print response.read()
except urllib2.URLError,e:
	 if hasattr(e,"code"):
		 print e.code
	 if hasattr(e,"reason"):
		 print e.reason
		 
