#coding=utf-8
#2017.9.24,Flash,��������ֵ

def make_shirt(logo="I love Python",size="XXL"):
	print "The shirt size is "+size+",and the logo is '"+logo+"'."
make_shirt("GitHub","M")
make_shirt()

print "============================��������ֵ=========================="
def get_formated_name(first_name,last_name):
	"""�������������"""
	full_name=first_name+' '+last_name
	return full_name
musician=get_formated_name("jimi",'hendrix')
print (musician)

print "==============================�����ֵ�==========================="
def person(name,sex,age,grade):
	person={"name":name,"sex":sex,"age":age,"grade":grade}
	return person
person=person("LiMing","1","18","Senior high school")
for k,v in person.items():
	print k+":"+v
