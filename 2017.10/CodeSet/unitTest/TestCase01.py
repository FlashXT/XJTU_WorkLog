#coding=utf-8
#2017.10.2,Flash,testcase01

import unittest
from name_function import get_formatted_name
from name_function import get_formatted_name2

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		"""能够正确地处理像Janis Joplin这样的姓名？"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name,'Janis Joplin')
	def test_first_last_middle_name(self):
		"""能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
		formatted_name = get_formatted_name2('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
	
unittest.main()
