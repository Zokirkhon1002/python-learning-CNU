# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:32:03 2021

@author: Zokirkhon
topic: Functions
"""


# 1
# n=3
# def func():
#     if n:
#         total=n
#         print(total)

# func();


# 2
# total = 0
# def mysum():
#     global total
#     total += 1
#     print(total)

# def yoursum():
#     global total
#     total += 3
#     print(total)

# mysum() # 1
# mysum() # 2
# mysum() # 3
# yoursum() # 6
# yoursum() # 9
# yoursum() # 12






###3
from b import func_b
var=100
def func_a():
    print(var)
func_b()
func_a()








###4
##Closures
print(dir(func_a.__closure__))