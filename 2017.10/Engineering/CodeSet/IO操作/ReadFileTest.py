#coding=utf-8
#2017.10.1,Flash,Read file

#1.��ȡ�����ļ�
with open("python_notes.txt") as file1:
	contents=file1.read()
print contents
print "======================================="
#2.���ж�ȡ�ļ�
with open("python_notes.txt") as file2:
	for line in file2.readlines():
		print line.rstrip()
print "======================================="
#3.���ж�ȡ�ļ�
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

