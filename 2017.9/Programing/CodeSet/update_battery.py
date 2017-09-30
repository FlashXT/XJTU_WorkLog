#coding=utf-8
#2017.9.29,Flash,example of extends
#coding=utf-8
#2017.9.28,Flash,extend

class Car(object):
	'''����������'''
	def __init__(self,maker,model,year,power):
		self.maker=maker
		self.model=model
		self.year=year
		self.power=power
	def getinfo(self):
		self.info=self.year.title()+" "+self.maker.title()+" "+self.model.title()
		return self.info
	def read_odometer(self):
		print ("This car has "+str(self.odometer_reading)+ " miles on it.")
	def update_odometer(self,mileage):
		if mileage >= self.mileage:
			self.odometer_reading=mileage
		else:
			print ("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading+=miles
	def fill_gas_tank(self):
		print ("This car has one gas tank!")
		
class ElectricCar(Car):
	'''����綯�����࣬�̳���������'''
	def __init__(self,maker,model,year,power):
		super(ElectricCar,self).__init__(maker,model,year,power)
		#self.battery_size=70
		self.battery=Battery()
	def fill_gas_tank(self):
		print ("This electriccar has no gas tank!")
	def describe_battery(self):
		"""��ӡһ��������ƿ��������Ϣ"""
		print("This car has a " + str(self.battery.battery_size) + "-kWh battery.")


class Battery():
	'''������'''
	def __init__(self,battery_size=70):
		'''��ʼ����ƿ������'''
		self.battery_size=battery_size
	def describe_battery(self):
		'''��ӡ�����Ϣ'''
		print("This car has a "+str(self.battery_size)+"-kwh battery.")
	def get_range(self):
		"""��ӡһ����Ϣ��ָ����ƿ���������"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	def update_battery(self):
		if self.battery_size<85:
			self.battery_size=85
			print"updating..."


my_tesla=ElectricCar('tesla','model S','2016','500')

print(my_tesla.getinfo())
my_tesla.fill_gas_tank()
my_tesla.describe_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
