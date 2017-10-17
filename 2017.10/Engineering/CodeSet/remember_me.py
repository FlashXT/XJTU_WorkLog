#coding=utf-8
#2017.10.2,Flash,json dump()&load()
import json


filename="username.json"
try:
	with open(filename,'r') as file2:
		content =json.load(file2)
except IOError:
	username=raw_input("What's your name ? ")
	with open(filename,"w") as file1:
		json.dump(username,file1)
	print "\nWe'll remember you when you come back,"+username+"!"
	print "============================================="
else:
	print "Welcome back,"+content+"!"
