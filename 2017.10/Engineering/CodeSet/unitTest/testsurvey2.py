#coding=utf-8
#2017.10.3,Flash,testsurvey

import unittest
from TestClass_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""���AnonymousSurvey��Ĳ���"""
	
	def setUp(self):
		"""
		����һ����������һ��𰸣���ʹ�õĲ��Է���ʹ��
		"""
		question="What language did you first learn to speak ?"
		self.my_survey=AnonymousSurvey(question)
		self.responses=['English','Chinese','Korean']
		
	def test_store_single_response(self):
		"""���Ե����𰸻ᱻ���Ƶش洢"""
		
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
	def test_store_single_response2(self):
		"""���������𰸻ᱻ���Ƶش洢"""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
unittest.main()
