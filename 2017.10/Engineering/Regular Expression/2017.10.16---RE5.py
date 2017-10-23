#coding=utf-8
#2017.10.16,Flash,IO
print "========Re========"
import re

pattern = re.compile(r'\w')
result1 = re.findall(pattern,"hello 1237")
if result1 :
	print result1
else:
	print "Match nothing! "
