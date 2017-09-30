#coding=utf-8
#2017.9.30,Flash,chapter10,IO

filename = 'pi_digits.txt'
print "=================================="
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
print "=================================="
print(contents.rstrip())
print "=================================="

with open(filename) as file_object:
	for line in file_object:
		print(line)
print "=================================="	
with open(filename) as file_object:
	lines=file_object.readlines()
	for line in lines:
		print(line.rstrip())		


