#coding=utf-8
#2017.9.24,Flash,�б�����������

def function1(names):
	for name in names:
		print name.title()+" ,welcome !"
	return len(names)

names=["AAA","BBB","CCC"]
function1(names)

print "================================================================"
def print_models(unprinted_designs, completed_models):
	"""
	ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
	��ӡÿ����ƺ󣬶������Ƶ��б�completed_models��
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# ģ������������3D��ӡģ�͵Ĺ���
		print("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""��ʾ��ӡ�õ�����ģ��"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t"+completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print "unprinted_designs = "+str(unprinted_designs)
print "completed_models = "+str(completed_models)

print "================================================================"
def print_models(unprinted_designs, completed_models):
	"""
	ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
	��ӡÿ����ƺ󣬶������Ƶ��б�completed_models��
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# ģ������������3D��ӡģ�͵Ĺ���
		print("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""��ʾ��ӡ�õ�����ģ��"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t"+completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models[:])
show_completed_models(completed_models)
print "unprinted_designs = "+str(unprinted_designs)
print "completed_models = "+str(completed_models)
	


