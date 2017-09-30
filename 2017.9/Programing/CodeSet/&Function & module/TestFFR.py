#coding=utf-8
#2017.9.25,Flash,º¯ÊýÓëÄ£¿é
print "==================================="
import fourFundamentalRules

print fourFundamentalRules.AddNums(1,2)
print fourFundamentalRules.SubNums(1,2)
print fourFundamentalRules.Multiplication(3,6)
print fourFundamentalRules.Divide(3,6)

print "===================================="

import fourFundamentalRules as FFR

print FFR.AddNums(1,2)
print FFR.SubNums(1,2)
print FFR.Multiplication(3,6)
print FFR.Divide(3,6)

print "===================================="

from fourFundamentalRules import *

print AddNums(1,2)
print SubNums(1,2)
print Multiplication(3,6)
print Divide(3,6)

print "===================================="

from fourFundamentalRules import AddNums as An,SubNums as Sn,Multiplication as Mu,Divide as Div

print An(1,2)
print Sn(1,2)
print Mu(3,6)
print Div(3,6)

