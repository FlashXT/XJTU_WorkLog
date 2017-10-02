#coding=utf-8
#2017.10.2,Flash,json dump()&load()
import json

def get_stored_username():
	"""����洢���û������ͻ�ȡ��"""
	filename="username.json"
	try:
		with open(filename,'r') as file2:
			content =json.load(file2)
	except IOError:
		return None
	else:
		return content
def get_new_username():
	"""��ʾ�����û���"""
	username=raw_input("What's your name ? ")
	filename="username.json"
	with open(filename,"w") as file1:
		json.dump(username,file1)
	return username
def greet_user():
	"""�ʺ��û�����ָ��������"""
	username=get_stored_username()
	if username:
		boo=raw_input("Is your name "+username+"?(Y/N)")
		if boo=="Y":
			print "Welcome back,"+username+"!"	
		else:
			username=get_new_username()
			print "\nWe'll remember you when you come back,"+username+"!"
	else:
		username=get_new_username()
		print "\nWe'll remember you when you come back,"+username+"!"
			
greet_user()

