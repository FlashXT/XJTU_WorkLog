#coding=utf-8
#2017.9.29,Flash,My_Car01
from Car import Car
from eCar_Battery import ElectricCar,Battery 

my_newCar=Car("Audi","A5","2016")
print(my_newCar.get_descriptive_name())
my_newCar.odometer_reading = 23
my_newCar.read_odometer()
print"========================================="
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print"========================================="
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
