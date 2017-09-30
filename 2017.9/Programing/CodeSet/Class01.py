#coding=utf-8
#2017.9.26,Flash,Class

class Dog():
	'''定义Dog类'''
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name=name
		self.age=age
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title()+" is now sitting.")
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title()+" rolled over!")
		
my_dog=Dog("QQQ",6)
print my_dog.name
print my_dog.age

my_dog2=Dog("AAA",8)
print my_dog2.name
print my_dog2.age
my_dog.sit()
my_dog.roll_over()
print "====================="
class Restaurant():
	"""定义餐馆类"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def descirbe_restaurant(self):
		print self.restaurant_name
		print self.cuisine_type
	def open_restaurant(self):
		print "open_restaurant"
		
rest=Restaurant("WuTongYuan","chao")
print rest.restaurant_name
print rest.cuisine_type
rest.descirbe_restaurant()
rest.open_restaurant()
