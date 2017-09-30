#coding=utf-8
#2017.9.29,Flash,Python±ê×¼¿â

from collections import OrderedDict
from random import randint
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

class Die():
	def __init__(self,sides=6):
		self.sides=sides
	def roll_die(self,times):
		for time in range(1,times+1):
			print randint(1,self.sides)
die=Die(10)
die.roll_die(10)
		
