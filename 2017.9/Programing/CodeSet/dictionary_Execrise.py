#coding=utf-8
#2017.9.22,Flash,�ֵ�ϰ����ϰ

#1.�ֵ�Ƕ���ֵ䣬�洢�û���Ϣ

people={
	"WangMao":{"Name":"Mao","Age":"20","Grade":"1"},
	"DaLi":{"Name":"Li","Age":"21","Grade":"1"},
	"LiBai":{"Name":"Bai","Age":"20","Grade":"1"}
	}
for user,info in people.items():
	print user+":"
	for k,v in info.items():
		print "\t"+k+":"+v
	print"========================================="

#2.�ֵ�Ƕ���б��洢�û�ƫ����Ϣ
favorite_places={
    "Mao":['DaLi','ErSea','Mount.Tai'],
    "Zhou":["Mount.Hua","LongMenShiKu","DunHuang"],
    "Liu":["DaBieShan","YanAn","NanJing"]
    }	
for name,places in favorite_places.items():
	print "The favorite places of "+name+" are :"
	for place in places:
		print "\t"+place
	print "========================================="

#
