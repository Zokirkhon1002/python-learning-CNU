# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:15:13 2021

@author: Zokirkhon
Homework - 4.11
"""


"""
Task: The program below is a program that obtains the result shown 
in the table on the right by using class inheritance and polymorphism. 
Write classes Dog and Cat to get the output

직무: 아래 프로그램은 클래스의 상속과 다형성을 사용하여 오른쪽 표와 같은 결과를 얻은 프로그램이다. 
출력을 얻기 위한 클래스 Dog와 Cat를 작성하시오
"""


class Animal:
    def __init__(self,name):
        self.name = name;
    def speak(self):
        return "Can not be understandable"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animalList = [Dog("dog1"),Dog("dog2"),Cat("cat1")]
for a in animalList:
    print(f"{a.name} : {a.speak()}")