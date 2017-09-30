#coding=utf-8
#2017.9.18,Flash，列表推导式，轻量级循环
list=[x*x for x in range(10) if x%3==0]
print "list="+str(list)
print "=============================================================================="
list1=[(x,y) for x in range(3) for y in range(3)]
print "list1="+str(list1)
print "=============================================================================="
list2=[]
for x in range(3):
	for y in range(3):
		list2.append((x,y))
print "list2="+str(list2)

print "==================================列表切片===================================="
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print   "players="+str(players[0:])
print   "players="+str(players[:5])
print   "players="+str(players[-3:]) #输出末尾3个元素

print "==================================列表复制===================================="
list01=[1,2,3,4]
list02=list01[:]
list03=list01
print "list01="+str(list01)
print "list02="+str(list02)
print list01==list02 and "list01==list02" or "list01!=list02"
print list01 is list02 and "list01 is list02" or "list01 isn't list02"
print list01 is list03 and "list01 is list03" or "list01 isn't list03"
print "================================条件表达式===================================="

print 'aaa' if 1 else 'bbb'
print 1 and 'aaa' or 'bbb'

print "===========================输出列表中间三个元素==============================="

list06=[1,2,3,4,5,6,7,8,9,10]
print "len(list06)="+str(len(list06))
print (len(list06)-1)/2
print list06[len(list06)/2-1:len(list06)/2+2]
