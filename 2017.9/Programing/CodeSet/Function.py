#coding=utf-8
#2017.9.23,Flash��Function

#��������
def greet_user():
	"""��ʾ�򵥵��ʺ���"""
	print("Hello!")
greet_user()

def greetUser(username):
	print username + ", Welcome !"
greetUser("Python")
print "======================="
def Div(a,b):
        print str(a)+"/"+str(b)+"="+str(a/b)
Div(18,3)
print"============================"
#def describe_pet(animal_type="dog",pet_name):  
#			"""��ʾ�������Ϣ"""
#			print("\nI have a " + animal_type + ".")
#			print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(pet_name='harry') #�ؼ��ֲ���

#����Ĭ��ֵ��������Ĭ��ֵ����֮ǰ
def describe_pet(pet_name,animal_type="dog"):  
	"""��ʾ�������Ϣ"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry')  
describe_pet('DaMao')
describe_pet(animal_type="Cat",pet_name='DaGou')	
