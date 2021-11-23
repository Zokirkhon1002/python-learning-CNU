# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:36:57 2021

@author: Zokirkhon
Homework - 4.6
"""


"""
Task: Write the output of the following program

직무: 다음 프로그램의 출력 결과를 쓰시오
"""





class Rectangle:
	def __init__(self, side=0):
		self.side = side
	def getArea(self):
		return self.side*self.side
	    
def printAreas(r, n):
	while n >= 1:
		print(r.side, "\t", r.getArea())
		r.side = r.side + 1
		n = n - 1
		
myRect = Rectangle()
count = 5
printAreas(myRect, count)
print("최종 사각형 변의 길이=", myRect.side)
print("반복횟수=", count)

"""
Output:
0 	 0
1 	 1
2 	 4
3 	 9
4 	 16
최종 사각형 변의 길이= 5
반복횟수= 5
"""
