#coding=utf-8
#2017.10.10,Regular Expression

import re

pattern = re.compile(r'hello')
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')

if result1:
	#使用Match获得分组信息
	print str(result1.pos)+"-"+str(result1.endpos)+"-"+str(result1.lastindex)+"-"+str(result1.lastgroup)
	print result1.group()
	print 
else:
	print "1匹配失败！"

if result2:
	#使用Match获得分组信息
	print result2.group()
else:
	print "2匹配失败！"

if result3:
	#使用Match获得分组信息
	print result3.group()
else:
	print "3匹配失败！"
if result4:
	#使用Match获得分组信息
	print result4.group()
else:
	print "4匹配失败！"
	

