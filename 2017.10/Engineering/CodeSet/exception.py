#coding=utf-8
#2017.10.2,Flash,exception
a= raw_input("input:")
b= raw_input("input:")


def add(a,b):

    try:
        c=int(a) + int(b)
    except ValueError:
        print " ‰»Î¿‡–Õ¥ÌŒÛ£°"
    else:
        print "C = "+str(c)
    
while True:    
		add(a,b)
		i=raw_input("quit?\n")
		if i.upper()=="Y":
			break
			

