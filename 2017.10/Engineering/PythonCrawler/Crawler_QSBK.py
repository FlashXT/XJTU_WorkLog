#coding=utf-8
#2017.10.6,Flash,ôÜÊÂ°Ù¿Æ

import urllib
import urllib2
import re
url = "https://www.qiushibaike.com/hot/page/1/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
header= {"User-Agent":user_agent}

try:
	request = urllib2.Request(url,headers = header)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile('<div.*?id="content"class="main">.*?<div.*?id=(.*?).*?class.*?>')
	items = re.findall(pattern,content)

	for item in items:
			print item
	print response.read()
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason

	

