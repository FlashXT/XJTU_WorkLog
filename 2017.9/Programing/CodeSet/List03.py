#coding=utf-8
#组织列表，2017-9-16，Flash
list=[1,2,34,56,5,76,76,898,76,42,21,36]
print "list="+str(list)+"\n"
#对list使用sort()方法
print "①sort()方法："
v1=list.sort()
print "\tlist.sort()\t\t\t===>\tlist="+str(list)+",返回值="+str(v1)

#对list使用sort()方法+reverse=True参数：
print "  sort(reverse=True):"
v2=list.sort(reverse=True)
print "\tlist.sort(reverse=True)\t\t===>\tlist="+str(list)+",返回值="+str(v2)

#对list使用sorted()方法：
print "②sorted()方法："
list=[1,2,34,56,5,76,76,898,76,42,21,36]

v3=sorted(list)
print "\tsorted(list)\t\t\t===>\tlist="+str(list)+",\n\t\t\t\t\t\t返回值="+str(v3)
#对list使用sorted()方法+reverse=True参数：
print "  sorted(reverse=True):"
v4=sorted(list,reverse=True)
print "\tsorted(list,reverse=True)\t===>\tlist="+str(list)+",\n\t\t\t\t\t\t返回值="+str(v4)
print "\n===================================================我是分割线===================================================\n"
cars=['bmw', 'audi', 'toyota', 'subaru']

#对列表使用reverse()方法
print "cars="+str(cars)+"\n"
print"③reverse()方法："
v4=cars.reverse()
print "\tcars.reverse()\t\t\t===>\tcars="+str(cars)+",返回值="+str(v4)

#获取列表长度
print"④len()方法："
print "\tlen(cars)\t\t\t===>\tlen(cars)="+str(len(cars))+",返回值= list的长度"
