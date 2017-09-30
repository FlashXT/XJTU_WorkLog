#coding=utf-8
#2017.9.22,Flash,读取用户输入
message =raw_input("Tell me something, and I will repeat it back to you: ")
print(message)

count=0
while count<=10:
	print count
	count+=1


peiliao=raw_input("Which kind of peiliao do you want ?\n")

while peiliao!="quit":
	print "\nAdd "+peiliao+"."
	peiliao=raw_input("Anything more?")
