# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:50:56 2021

@author: Zokirkhon
Homework - 4.10
"""


"""
Task: In the program below, Dog inherits from Animal and uses it. 
Write the appropriate word in ( ) and write the output result.

직무: 아래 프로그램에서 Dog는 Animal을 상속 받아서 사용한다. 
( )에 적당한 단어를 쓰고, 출력 결과를 쓰시오
"""


class Animal:
    def __init__(self, name=""):
        self.name=name
    def eat(self):
        print("동물이 먹고 있습니다. ")
class Dog(Animal): #Animal
    def __init__(self, name):
        super().__init__(name) # super()
    def eat(self):
        print("강아지가 먹고 있습니다. ")
d = Dog('Merry')
print(d.name)
d.eat()
# Output:
# Merry
# 강아지가 먹고 있습니다. 


