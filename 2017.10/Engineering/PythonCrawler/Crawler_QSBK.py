#coding=utf-8
#2017.10.6,Flash,ôÜÊÂ°Ù¿Æ

import urllib
import urllib2
import re
 
page = 1
url = "https://www.qiushibaike.com/hot/page/"+str(page)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
header= {"User-Agent":user_agent}

try:
	request = urllib2.Request(url,headers = header)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<div class="thumb".*?src=(.*?)alt.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<a.*?<i class="number">(.*?)</i>',re.S)
	items = re.findall(pattern,content)

	for item in items:
			print item[0],item[1],item[2],item[3],item[4]
			
	print response.read()
	
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason

	

