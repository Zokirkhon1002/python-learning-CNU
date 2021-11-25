# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:15:19 2021

@author: Zokirkhon
"""

###1
# from fibo import fib, fib2, __name__

# fib(1000)
# print(fib2(1000))
# print(__name__)





###2
# import copy
# colors = ['red', 'blue', 'green']
# clone = colors

# clone[0] = 'black'
# print(colors)
# print(clone)
# print(id(colors), id(clone))
# print()

# colors = ['red', 'blue', 'green']
# clone = copy.deepcopy(colors)

# clone[0] = 'black'
# print(colors)
# print(clone)
# print(id(colors), id(clone))







###3
# from copy import deepcopy
# x=[1,2,3]
# lst=[1,2,x]
# lst1=deepcopy(lst)
# print(id(lst)==id(lst1))
# print(lst)
# print(lst1)
# lst1[2][1]=4
# print(lst)
# print(lst1)





###4
# import keyword
# name = input('Enter a name: ')
# if keyword.iskeyword(name):
#     print(f"{name} is an abbreviation")
#     print("Below is the full list of keywords")
#     print(keyword.kwlist)
# else:
#     print(f"{name} is not an abbreviation")







###5
# import random


# random.seed(10)
# for i in range(5):
#     print(random.randint(1,100), end=" ")
# print()
# random.seed(10)


# for i in range(5):
#     print(random.randint(1,100), end=" ")
# print()
# random.seed(10)

# for i in range(5):
#     print(random.randint(1,100), end=" ")






###6
import random
save_state = random.getstate()

print(random.randrange(0,20))
print(random.randrange(0,20))
print(random.randrange(0,20))

random.setstate(save_state)
print(random.randrange(0,20))
print(random.randrange(0,20))
print(random.randrange(0,20))