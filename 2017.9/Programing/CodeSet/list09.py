#coding=utf-8
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for rt in requested_toppings:
	if rt in available_toppings:
		print ("Adding "+ rt +".")
	else:
		print("Sorry,we don't have"+rt+".")
print("\nFinished making your pizza!")
print"======================="
users=['admin','FlashXT','LiJie','baidu','Alibaba']
#users=[]
if users:
	for user in users:
		if user=='admin':
			print "Hello,admin!"
		else:
			print str(user)+" welcome!"
else:
	print "Find no uesrs !"
