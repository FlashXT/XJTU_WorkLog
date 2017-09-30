#coding=utf-8
def Welcome():
   print"=========================="
   for i in range(len(guest)):
	 print guest[i]+",welcome!"
def Del1():
	print"========================="
	i=0
	while(len(guest)>2):
		print guest.pop()+",sorry!"
def Del2():
	print"========================="
	i=0
	while(len(guest)>0):
		print guest.pop()+",sorry!"		
guest=['XiaoMing','XiaoFang','XiaoHong']
Welcome()
print"=========================="
print guest.pop(2)+".can't be here!"
guest.insert(2,'XiaoHua')
Welcome()
print "I find a bigger desk!"
guest.insert(0,'LiHua')
guest.insert(3,'WangDaMao')
guest.append('WangMing')
Welcome()
print "Sorry,I can only invite two guests!"
print guest
Del1()
Welcome()
Del2()
print guest
