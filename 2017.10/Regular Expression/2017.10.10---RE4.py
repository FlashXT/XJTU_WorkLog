#coding=utf-8
#2017.10.10,Flash,

import re
pattern = re.compile(r'\d+')
print re.split(pattern,"one1two2three3four4")
print re.findall(pattern,"one1two2three3four4")


for m in re.finditer(pattern,"one1two2three3four4"):
	print m.group()

pattern2 = re.compile(r'(\w+) (\w+)')

s="i say,hello world!"
print re.sub(pattern2,r'\2 \1',s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern2,func, s)

print re.subn(pattern2,r'\2 \1',s)
print re.subn(pattern2,func, s)
