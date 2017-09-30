#coding=utf-8
#2017.9.29,Flash,electricCar&Battery

from Car01 import Car
class Battery():
	"""һ��ģ��綯������ƿ�ļ򵥳���"""
	def __init__(self, battery_size=70):
		"""��ʼ����ƿ������"""
		self.battery_size = battery_size
	def describe_battery(self):
		"""��ӡһ��������ƿ��������Ϣ"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def get_range(self):
		"""��ӡһ��������ƿ������̵���Ϣ"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
class ElectricCar(Car):
	"""ģ��綯�����Ķ���֮��"""
	def __init__(self, make, model, year):
		"""
		��ʼ����������ԣ��ٳ�ʼ���綯�������е�����
		"""
		super(ElectricCar,self).__init__(make, model, year)
		self.battery = Battery()
