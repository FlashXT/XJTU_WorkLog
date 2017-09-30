#coding=utf-8
#2017.9.22,Flash,list & dictionary 嵌套
alien_0={"color":"green","points":5}
alien_1={"color":"yellow","points":10}
alien_2={"color":"red","points":15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print (alien)
pizza={
	'crust':'think',
	'toppings':['mushrooms','extra cheese'],
	
	}
print("You order a " +pizza['crust']+"-crust pizza"+ 
	  "with the following topping:")
for topping in pizza["toppings"]:
	print ("\t"+topping)
print "====================================="
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
print"======================================="

users={
   "XiaoMing":{"Name":"Mr.Ming","Age":23,"location":"A"},
   "XiaoHua":{"Name":"Mr.Hua","Age":22,"location":"B"},
   "XiaoHong":{"Name":"Mr.Hong","Age":20,"location":"C"},
   }
for user in users.keys():
	print user+":"
	for key,value in users[str(user)].items():
		print "\t"+key.title()+":"+str(value)
	print "=========="
