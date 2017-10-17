#coding=utf-8
#2017.10.3,Flash,employee class

class Employee():
	"""定义员工类"""
	def __init__(self,first_name,last_name,salary):
		self.first_name=first_name
		self.last_name=last_name
		self.salary=salary
	def give_raise(self,increasment=5000):
		self.salary+=increasment
		return self.salary
	
