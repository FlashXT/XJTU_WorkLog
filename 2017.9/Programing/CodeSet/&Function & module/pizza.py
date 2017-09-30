#coding=utf-8
#2017.9.25,Flash,Function & module

def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " +str(size)+"-inch pizza with the following toppings :")
	for topping in toppings:
		print("- "+topping)
