#coding=utf-8
#2017.9.25,Flash,�����������������Ĳ���
#���������������Ĳ���
def make_pizza(*toppings):
	for topping in toppings:
		print "Adding "+topping+"!"
	print "Finished !"

make_pizza("111")
make_pizza("AAA","BBB","CCC","DDD")
print"===================================="

#���ʹ��λ��ʵ�κ���������ʵ��
def make_pizza(size,*toppings):
	print "Making a "+size +" inch pizza!"
	for topping in toppings:
		print "Adding "+topping+" ..."
	print "Finishing your pizza !"
make_pizza("20","BBB","CCC","DDD")	

print"===================================="

#ʹ�����������Ĺؼ���ʵ��
def userinfos(first,last,**userinfo):
	"""����һ���ֵ䣬���а����û���Ϣ"""
	profile={}
	profile["first_name"]=first
	profile["last_name"]=last
	for key,value in userinfo.items():
		profile[key]=value
	return profile
userinfo=userinfos("First","Last",location="China",City="Xi'an")
for key,value in userinfo.items():
	print str(key) +" : "+ str(value)+";"
print"===================================="

#�����������
def make_sandwich(*inners):
	for inner in inners:
		print "Adding "+ str(inner) +"!"
	return inners
make_sandwich("AAA","BBB","CCC","DDD")
print "\n"
make_sandwich("EEE","FFF","GGG")
print "\n"
make_sandwich("HHH")

print"===================================="
#���������ֵ��
def cars(maker,model,**infos):
	carinfo={}
	carinfo["maker"]=maker
	carinfo["model"]=model
	for k,v in infos.items():
		carinfo[k]=v
	return carinfo

info=cars("Tesla","model 3",color="silver",Power="500kw")
for k,v in info.items():
	print k+" : "+v+ ";" 
 	


	
