#coding=utf-8
#2017.10.1,Flash,test replace()

message = "I really like dogs dogs dogs."

print message.replace("dogs","cats")
print message.replace("dogs","cats",2)

"""replace()函数操作对原字符串没有影响，即操作结果无法保存，
	可以利用重新赋值为元字符串的方法保存操作结果。"""
	
"""	replace()方法返回当前old换成new，可选择的替代限制到最大数量的字符串的副本。
	语法:	str.replace(old, new[, max])

	参数:
			old -- 这是要进行更换的旧子串。
			new -- 这是新的子串，将取代旧的子字符串。
			max -- 如果这个可选参数max值给出，替换不超过 max 次。
"""
