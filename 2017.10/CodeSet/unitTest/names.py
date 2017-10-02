#coding=utf-8
#2017.10.2,Flash,names
from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
	first = raw_input("\nPlease give me a first name: ")
	last = raw_input("Please give me a last name: ")
	flag=raw_input("Continue?(Y/N)")
	if flag == 'N':
		break
	else:
		pass
formatted_name = get_formatted_name(first, last)
print("Neatly formatted name: \n" + formatted_name + '.')

