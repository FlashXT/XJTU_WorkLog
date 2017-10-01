#coding=utf-8
#2017.10.1,Flash,Read file

#1.读取整个文件
with open("python_notes.txt") as file1:
	contents=file1.read()
print contents
print "======================================="
#2.按行读取文件
with open("python_notes.txt") as file2:
	for line in file2.readlines():
		print line.rstrip()
print "======================================="
#3.按行读取文件
with open("python_notes.txt") as file3:
	lines=file3.readlines()
	
for line in lines:
	print line.rstrip()
print "======================================="

with open("python_notes.txt") as file2:
	line=file2.readline()
	while line:
		line=line.replace('Python','C')
		print line.rstrip()
		line=file2.readline()

