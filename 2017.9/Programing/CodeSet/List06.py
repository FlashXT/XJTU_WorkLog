#coding=utf-8
#2017.9.18, Flash,创建数值列表；

#range()函数使用；
for i in range(1,5):
	print i
print "=========================================="
for i in range(5):
	print i
print "=========================================="
for i in range(0,9,3):
	print i
#使用range()函数创建数值列表；
print "=========================================="
nums=list(range(10))
print nums
print "=========================================="
list=[]

for i in range(1,11):
	list.append(i**2)
print list
print "=========================================="
print "listmin="+str(min(list))
print "listmax="+str(max(list))
print "listsum="+str(sum(list))
print "=========================================="
list2=[value**2 for value in range(1,11)]
print list2
print "=========================================="
list3=[]
for i in range(1,1000000+1):
   list3.append(i)
print "list3min="+str(min(list3))
print "list3max="+str(max(list3))
#print "listsum="+str(sum(list3))
print "=========================================="
list4=[value for value in range(1,20,2)]
#print list4
for i in list4:
	 print i
print "=========================================="
list4=[value for value in range(3,30+1,3)]
for i in list4:
	print i
print "=========================================="
list5=[value**3 for value in range(1,10+1)]
for i in range(len(list5)):
	print list5[i]
print "=========================================="
