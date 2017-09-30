#coding=utf-8
#2017.9.29,Flash,users & Admin
class Users(object):
	def __init__(self,name,nums,grade,tel):
		self.name=name
		self.nums=nums
		self.grade=grade
		self.tel=tel
	def userInfo(self):
		print self.name+" "+self.nums+" "+self.grade+" "+self.tel
	def getTel(self):
		print self.tel
class Admin(Users):
	def __init__(self,name,nums,grade,tel,address):
		super(Admin,self).__init__(name,nums,grade,tel)
		self.address=address
		self.privileges=["can add post","can delete post","can ban user"]
	def userInfo(self):
		print self.name+" "+self.nums+" "+self.grade+" "+self.tel+" "+self.address
	def show_privileges(self):
		print "the privileges of admin :".title()
		for privilege in self.privileges:
			print "\t"+privilege.title()
admin=Admin("XiaoDingDang","32131","2","13232434","Xi'an")

admin.userInfo()
admin.show_privileges()
