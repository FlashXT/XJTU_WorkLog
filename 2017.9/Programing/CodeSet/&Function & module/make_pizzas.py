#coding=utf-8

#方法一

import pizza
pizza.make_pizza(16,"pepperoni")
pizza.make_pizza(12,"AAA","BBB","CCC","DDD")

#方法二
from pizza import make_pizza
make_pizza(16,"pepperoni")
make_pizza(12,"AAA","BBB","CCC","DDD")
