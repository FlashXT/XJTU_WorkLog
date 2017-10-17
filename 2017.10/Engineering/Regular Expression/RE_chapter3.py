#coding=utf-8
#2017.10.10,Flash,

import re
str="How a Ship having passed the Country Line was driven \
Country fsfsd Country."
print str
pattern = re.compile('^How.*Country\.$')
print re.findall(pattern,str)
