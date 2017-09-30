#coding=utf-8
#2017.9.21,Flash,¼ì²âÓÃ»§Ãû³åÍ»

current_users=["baidu","ALI","Tencent","MI","Apple"]
new_users=["Ali","Baidu","XIMI","Lenovo","OPPO","MEIZU"]

for new_user in new_users:
	if new_user.lower() in current_users or new_user.upper() in current_users or new_user.title() in current_users :
		print "Sorry,Please change your user name "+new_user+"!"
	else :
		current_users.append(new_user)
print "=====================0~9============================="
nums=[1,2,3,4,5,6,7,8,9]

for i in nums:
	if i == 1:
		print str(i)+"st"
	elif i == 2:
		print str(i)+"nd"
	elif i == 3:
		print str(i)+"rd"
	else:
		print str(i)+"th"

