#coding=utf-8
#2017.10.2,Flash,unittest

def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ' ' + last
	return full_name.title()
def get_formatted_name2(first,last,middle=' '):
	"""Generate a neatly formatted full name."""
	full_name = first +' '+middle+' '+last
	return full_name.title()
