#coding=utf-8
#��֯�б�2017-9-16��Flash
list=[1,2,34,56,5,76,76,898,76,42,21,36]
print "list="+str(list)+"\n"
#��listʹ��sort()����
print "��sort()������"
v1=list.sort()
print "\tlist.sort()\t\t\t===>\tlist="+str(list)+",����ֵ="+str(v1)

#��listʹ��sort()����+reverse=True������
print "  sort(reverse=True):"
v2=list.sort(reverse=True)
print "\tlist.sort(reverse=True)\t\t===>\tlist="+str(list)+",����ֵ="+str(v2)

#��listʹ��sorted()������
print "��sorted()������"
list=[1,2,34,56,5,76,76,898,76,42,21,36]

v3=sorted(list)
print "\tsorted(list)\t\t\t===>\tlist="+str(list)+",\n\t\t\t\t\t\t����ֵ="+str(v3)
#��listʹ��sorted()����+reverse=True������
print "  sorted(reverse=True):"
v4=sorted(list,reverse=True)
print "\tsorted(list,reverse=True)\t===>\tlist="+str(list)+",\n\t\t\t\t\t\t����ֵ="+str(v4)
print "\n===================================================���Ƿָ���===================================================\n"
cars=['bmw', 'audi', 'toyota', 'subaru']

#���б�ʹ��reverse()����
print "cars="+str(cars)+"\n"
print"��reverse()������"
v4=cars.reverse()
print "\tcars.reverse()\t\t\t===>\tcars="+str(cars)+",����ֵ="+str(v4)

#��ȡ�б���
print"��len()������"
print "\tlen(cars)\t\t\t===>\tlen(cars)="+str(len(cars))+",����ֵ= list�ĳ���"
