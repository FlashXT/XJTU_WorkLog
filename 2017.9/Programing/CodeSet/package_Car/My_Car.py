#coding=utf-8
#2017.9.29,Flash,importclass

from Car import Car,ElectricCar #import语句让Python打开模块car，并导入其中的Car类

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
