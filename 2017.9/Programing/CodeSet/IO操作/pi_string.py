#coding=utf-8
#2017.9.30,Flash,IO
print "=================================="
filename="pi_digits.txt"
pi_string=""
with open(filename) as file_object:
	lines=file_object.readlines()
for line in lines:
	pi_string+=line.strip()
print "pi_string="+pi_string

filename="pi_million_digits.txt"
pi_string=""
with open(filename) as file_object:
	lines=file_object.readlines()
for line in lines:
	pi_string+=line.strip()
print "pi_string="+pi_string[0:52]+"..."
birthday=102094

print str(birthday) in pi_string
