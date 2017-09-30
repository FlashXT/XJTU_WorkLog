#coding=utf-8
#2017.9.23,Flash，Function

#函数定义
def greet_user():
	"""显示简单的问候语"""
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
#			"""显示宠物的信息"""
#			print("\nI have a " + animal_type + ".")
#			print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(pet_name='harry') #关键字参数

#将无默认值参数放在默认值参数之前
def describe_pet(pet_name,animal_type="dog"):  
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry')  
describe_pet('DaMao')
describe_pet(animal_type="Cat",pet_name='DaGou')	
