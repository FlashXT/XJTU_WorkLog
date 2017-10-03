#coding=utf-8
#2017.10.3,Flash, test employee
import unittest
from Employee import Employee

class Testemployee(unittest.TestCase):
	"""≤‚ ‘employee¿‡"""
	def setUp(self):
		self.employee=Employee("Flash","XT",200000)
	def test_give_default_salary(self):
	    self.assertEqual(205000,self.employee.give_raise())
	def test_give_custom_salary(self):
	    self.assertEqual(210000,self.employee.give_raise(10000))
	
unittest.main()
