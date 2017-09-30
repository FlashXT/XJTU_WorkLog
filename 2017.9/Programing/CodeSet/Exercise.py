#coding=utf-8
#2017.9.21,Flas和，练习近期学习知识的使用
#外星人颜色1
print "=========================外星人颜色1======================="
alien_color=raw_input("Input the color of alien:")
if alien_color.lower() =="green":
   print "You get five points!"
else: print " "
#外星人颜色2
print "=========================外星人颜色2======================="
alien_color=raw_input("Input the color of alien:")
if alien_color.lower() =="green":
   print "You get five points!"
else: 
	print "You get ten points! "
#外星人颜色2
print "=========================外星人颜色3======================="
alien_color=raw_input("Input the color of alien:")
if alien_color.lower() =="green":
   print "You get five points!"
elif alien_color.lower() == "yellow": 
	print "You get ten points! "	
else:
	print "You get fifth points! "
print"=======================favorite_fruits===================="
favorite_fruits=["Apple","banana","orange"]
if "Apple" in favorite_fruits:
	print "You really like Apple."
if "banana" in favorite_fruits:
	print "You really like banana."
else :
	print "You really like orange."
