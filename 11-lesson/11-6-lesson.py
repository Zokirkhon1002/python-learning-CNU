# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:48:51 2021

@author: Zokirkhon
Topic: Function
"""

###1
## co_routine example
# def co_routine():
#     total=0
#     while True:
#         n=(yield)
#         total+=n
#         print("total:",total)

# a=co_routine()
# a.__next__()
# a.send(10)
# a.send(10)
# a.send(30)
# print("type:",type(a))









###2
# def co_routine():
#     total=0
#     while True:
#         n=(yield)
#         total+=n
#         print("total:",total)

# a=co_routine()
# a.__next__()
# a.send(10)
# a.send(3)
# a.send(8)
# print("type:",type(a))








###3
import time
def coroutine():
    n=0
    while True:
        n=(yield n)
        time.sleep(1)
        if n%10==3 or n%10==6 or n%10==9:
            print("A: nothing")
        else:
            print("A:",n)
        n+=1
n=0
A=coroutine()
print(A.__next__())
while True:
    n=A.send(n)
    time.sleep(1)
    if n%10==3 or n%10==6 or n%10==9:
        print("b: nothing")
    else:
        print("b:",n)
    n+=1