#coding=utf-8
#2017.9.24,Flash,列表做函数参数

def function1(names):
	for name in names:
		print name.title()+" ,welcome !"
	return len(names)

names=["AAA","BBB","CCC"]
function1(names)

print "================================================================"
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# 模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
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
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# 模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t"+completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models[:])
show_completed_models(completed_models)
print "unprinted_designs = "+str(unprinted_designs)
print "completed_models = "+str(completed_models)
	


