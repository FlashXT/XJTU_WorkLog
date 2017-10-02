#coding=utf-8
#2017.10.2,Flash,exception

file1="cats.txt"
file2="dogs.txt"

def  Print(file_name):
	try :
		with open(file_name) as file_object:
			content=file_object.read()
	except  IOError:
		#print "File "+file_name+" not found!"
		pass
	else:
		print content.rstrip()
		
def CountWords(file_name):
	try :
		with open(file_name) as file_object:
			content=file_object.read()
	except  IOError:
		#print "File "+file_name+" not found!"
		pass
	else:
		print len(content.rstrip())
		print content.rstrip().lower().count("the")
		
files=['cats.txt','dogs.txt','A Little Princess .txt']

for file  in  files:
	CountWords(file)
	print"================="
	
