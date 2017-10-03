#coding=utf-8
#2017.10.3,Flash,testsurvey

import unittest
from TestClass_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试"""
	def test_store_single_response(self):
		"""测试单个答案会被妥善地存储"""
		question="What language did you first learn to speak ?"
		my_survey=AnonymousSurvey(question)
		my_survey.store_response("Chinese")
		self.assertIn("Chinese",my_survey.responses)
	def test_store_single_response2(self):
		"""测试三个答案会被妥善地存储"""
		question="What language did you first learn to speak ?"
		my_survey=AnonymousSurvey(question)
		responses=['English','Chinese','Korean']
		for response in responses:
			my_survey.store_response(response)
		for response in responses:
			self.assertIn(response,my_survey.responses)
unittest.main()
