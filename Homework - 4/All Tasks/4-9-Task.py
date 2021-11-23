# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:47:37 2021

@author: Zokirkhon
Homework - 4.9
"""


"""
Task: Write the result of the following program

직무: 다음 프로그램의 결과를 쓰시오
"""


class Bag:
	def __init__(self):
		self.data=[]
	def add(self, x):
		self.data.append(x)
	def add2(self, x):
		self.add(x)
		self.add(x)
		print(self.data)
bag=Bag()
bag.add2(5)
# Output:
# [5, 5]
bag.add2(7)
# Output:
# [5, 5, 7, 7]