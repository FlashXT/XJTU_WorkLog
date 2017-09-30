#coding=utf-8
#2017.9.27，Flash,Class实例练习

#1.servedNums()类
class servedNums():
	def __init__(self):
		self.servedNums=0
	def set_servedNums(self,n):
		self.servedNums=n
	def get_servedNums(self):
		return self.servedNums
	def increment_number_served(self):
		self.servedNums+=1
serNums=servedNums()

print serNums.get_servedNums()
for i in range(0,10):
	serNums.increment_number_served()
	print "waiting..."
	i+=1
print serNums.get_servedNums()

print "=================UserLogin=================="
#2.UserLogin()类

class userLogin():
	def __init__(self):
		self.login_attempts=0
	def get_loginattempts(self):
		return self.login_attempts
	def set_loginattempts(self,times):
		self.login_attempts+=times
	def increment_login_attempts(self):
		self.login_attempts+=1

ul=userLogin()

print  ul.get_loginattempts()
for i in range(0,100):
	ul.increment_login_attempts()
	i+=1
print ul.get_loginattempts()
		
		
