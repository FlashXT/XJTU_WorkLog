#coding=utf-8
#2017.10.10,Regular Expression

import re

pattern = re.compile(r'hello')
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')

if result1:
	#ʹ��Match��÷�����Ϣ
	print str(result1.pos)+"-"+str(result1.endpos)+"-"+str(result1.lastindex)+"-"+str(result1.lastgroup)
	print result1.group()
	print 
else:
	print "1ƥ��ʧ�ܣ�"

if result2:
	#ʹ��Match��÷�����Ϣ
	print result2.group()
else:
	print "2ƥ��ʧ�ܣ�"

if result3:
	#ʹ��Match��÷�����Ϣ
	print result3.group()
else:
	print "3ƥ��ʧ�ܣ�"
if result4:
	#ʹ��Match��÷�����Ϣ
	print result4.group()
else:
	print "4ƥ��ʧ�ܣ�"
	

