#coding=utf-8
#2017.9.29£¨Flash£¨example of extend 


class Restaurant(object):
	"""∂®“Â≤Õπ›¿‡"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def descirbe_restaurant(self):
		print self.restaurant_name.title()+"  "+self.cuisine_type.title()
	def open_restaurant(self):
		print "opening restaurant".title()+"at 8:00am."
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
		self.flavors=['milk', 'vanilla', 'chocolate','strawberry',
					  'green tea', 'taro']
	def IceCreamTastes(self):
		print"The tastes of our Ice Cream :"
		for taste in self.flavors:
			print "\t"+taste.title()

IceCream=IceCreamStand("Haagen Dazs","freezing")

IceCream.descirbe_restaurant()
IceCream.open_restaurant()
IceCream.IceCreamTastes()
		
	
	
	
