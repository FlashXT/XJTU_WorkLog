#coding=utf-8
#2017.10.10,Flash,Re search()

import re

pattern = re.compile(r"efghij")
#使用search()查找匹配的字符串，不存在能匹配的子串时将返回None
content="abcdefghijklmn"
m = re.search(pattern,content)

print "m.re:",m.re
print "\nm.string:",m.string
print "m.pos:",m.pos
print "m.endpos",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.groupdict():", m.groupdict()
print "m.start():", m.start()
print "m.end():", m.end()


