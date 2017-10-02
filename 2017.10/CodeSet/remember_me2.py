#coding=utf-8
#2017.10.2,Flash,json dump()&load()
import json

def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename="username.json"
	try:
		with open(filename,'r') as file2:
			content =json.load(file2)
	except IOError:
		return None
	else:
		return content
def greet_user():
	"""问候用户，并指出其名字"""
	username=get_stored_username()
	if username:
		print "Welcome back,"+username+"!"
	else:
		username=raw_input("What's your name ? ")
		filename="username.json"
		with open(filename,"w") as file1:
			json.dump(username,file1)
		print "\nWe'll remember you when you come back,"+username+"!"

greet_user()
