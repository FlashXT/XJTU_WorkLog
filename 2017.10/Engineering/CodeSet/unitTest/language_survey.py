#coding=utf-8
#2017.10.3,Flash,test class
from TestClass_survey import AnonymousSurvey


# ����һ�����⣬������һ����ʾ�����AnonymousSurvey����
question ="What language did you first learn to speak ?"
my_survey=AnonymousSurvey(question)

#��ʾ���Ⲣ�洢��
my_survey.show_question()
print "Enter 'q' at any time to quit.\n"
while True:
	response =raw_input("Language : ")
	if response == 'q':
		break
	my_survey.store_response(response)
	#��ʾ������
	print"\nThank you to everyone who participated in the survey !"
my_survey.show_results() 
