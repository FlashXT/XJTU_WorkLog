
import json
numbers=[2,3,5,7,11,13]
filename="numbers.json"
with open(filename,"w")as f_obj:
	json.dump(numbers,f_obj)
	
with open(filename,"r") as file:
	content=file.read()	
print content
print "=========================="

with open(filename) as f_obj:
	numbers=json.load(f_obj)
print numbers
