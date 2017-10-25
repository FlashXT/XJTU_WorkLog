#coding=utf-8
#2017.10.25,Flash,糗事百科

import urllib
import urllib2
import re
 
filename="qsbk.txt"
page = 1
#url = "https://www.qiushibaike.com/hot/page/"+str(page)
url = "https://www.qiushibaike.com/hot/3"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
header= {"User-Agent":user_agent}

try:
	request = urllib2.Request(url,headers = header)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats">.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<a.*?<i class="number">(.*?)</i>',re.S)
	items = re.findall(pattern,content)

	for item in items:
		haveImg = re.search("img",item[2])
		if  haveImg:	
			pattern2 = re.compile(r'src="(.*?)"',re.S)
			items2 = re.findall(pattern2,item[2])
			print "ID:",item[0]
			print "Content:",item[1]
			
			for it in items2:
				print "ImgAdd:\t",it
			print "点赞数:\t",item[3],"评论数:\t",item[4]
		else:
			print "ID:",item[0]
			print "Content:",item[1]
			print "ImgAdd:\t","None"
			print "点赞数:",item[3],"评论数:",item[4]
		print "========================================================"	
		#with open(filename,'a') as file_object:
		#	file_object.write(item[0].encode("UTF-8")+"\t"+item[1].encode("UTF-8")+"\t"+item[2].encode("UTF-8")+"\t"+item[3].encode("UTF-8")+"\t"+item[4].encode("UTF-8"))	
	print response.read()
	
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
else:
	print "OK!"
	

