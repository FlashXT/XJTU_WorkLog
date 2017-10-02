#coding=utf-8
#2017.10.2,Flash,citys
import unittest
from city_functions import Citys

class CityTestCase(unittest.TestCase):
	def test_Citys(self):
		city=Citys("Xi'an","China","143213211")
		self.assertEqual(city,"China Xi'an 143213211")
unittest.main()
