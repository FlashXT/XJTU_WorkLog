#coding=utf-8
#2017.9.24,Flash,函数返回值

def make_shirt(logo="I love Python",size="XXL"):
	print "The shirt size is "+size+",and the logo is '"+logo+"'."
make_shirt("GitHub","M")
make_shirt()

print "============================函数返回值=========================="
def get_formated_name(first_name,last_name):
	"""返回整洁的姓名"""
	full_name=first_name+' '+last_name
	return full_name
musician=get_formated_name("jimi",'hendrix')
print (musician)

print "==============================返回字典==========================="
def person(name,sex,age,grade):
	person={"name":name,"sex":sex,"age":age,"grade":grade}
	return person
person=person("LiMing","1","18","Senior high school")
for k,v in person.items():
	print k+":"+v
