#coding=utf-8
#�����б�2017.9.17��Flash
magicians=['alice','david','carolina']
print "magicians="+str(magicians)
print "=========================================="
#forѭ������Ԫ��
for i in range(len(magicians)):
	print magicians[i]
print "=========================================="
#foreach
for k in magicians:
	print k
print "=========================================="
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
