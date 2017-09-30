#coding=utf-8
#2017.9.22,Flash,字典习题练习

#1.字典嵌套字典，存储用户信息

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

#2.字典嵌套列表，存储用户偏好信息
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
