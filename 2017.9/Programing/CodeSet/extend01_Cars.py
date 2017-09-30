#coding=utf-8
#2017.9.28,Flash,��ļ̳�

class Car(object):
	"""����Car��"""
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		long_name=str(self.year)+" "+self.make+" "+self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has "+ str(self.odometer_reading)+"miles on it.")
		
	def update_odometer(self,mileage):
		if mileage >=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading+=miles
	def fill_gas_tank(self):
		"""��������"""
		print("This car a gas tank!")
class ElectricCar(Car):
	"""�綯���Ķ���֮��"""
	def __init__(self,make,model,year):
		"""��ʼ�����������"""
		super(ElectricCar,self).__init__(make,model,year)
		self.battery_size=70
	def describe_battery(self):
		"""��ӡһ������������Ϣ"""
		print("This car has a "+str(self.battery_size)+"-kwh battery.")
		
	def fill_gas_tank(self):
		"""�綯����û������"""
		print("This car doesn't need a gas tank!")
my_tesla=ElectricCar('tesla','model S',2016)


print my_tesla.get_descriptive_name()

print my_tesla.odometer_reading
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
			
