#coding=utf-8
#2017.10.1,Flash,write file

filename="programing.txt"

with open(filename,'w') as file_object:
	file_object.write("I love programing.\n")
	file_object.write("I love python.\n")
	file_object.write("I love creating new games.\n")
print "writing..."
with open(filename) as file_object:
	print file_object.read()


with open(filename,'a') as file_object:
	file_object.write("==============================================\n")
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
	file_object.write("I love learning Python and C.\n")
print "writing..."
with open(filename) as file_object:
	print file_object.read()

with open("guest.txt","w")as file1:
	line=raw_input("Please input your name:\n")
	while line!="quit":
	      file1.write(line+"\n")
	      line=raw_input("Please input your name:\n")
print "================="
with open("guest.txt") as file_object:
	print file_object.read()

print "===================================="
line=" "
while line!="quit":
	with open("guest.txt","a")as file1:
		  file1.write(line+"\n")
		  line=raw_input("Please input your reason:\n")
with open("guest.txt") as file_object:
	line=file_object.readline()
	while line:
		print line
		line=file_object.readline()
		
