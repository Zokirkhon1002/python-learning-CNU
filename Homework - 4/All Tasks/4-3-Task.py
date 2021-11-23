# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:56:27 2021

@author: Zokirkhon
Homework - 4.3
"""


"""
Task: Describe the encapsulation.
직무: 캡슐화(encapsulation)를 설명하시오.
"""



"""
English:

Encapsulation
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly 
and can prevent the accidental modification of data. To prevent accidental change, 
an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data 
that is member functions, variables, etc.





Korean:

캡슐화
캡슐화는 객체 지향 프로그래밍(OOP)의 기본 개념 중 하나입니다.
데이터를 래핑하는 아이디어와 한 단위 내에서 데이터에 대해 작동하는 방법을 설명합니다.
이것은 변수와 메소드에 직접 접근하는 것을 제한합니다.
데이터의 우발적인 수정을 방지할 수 있습니다. 우발적인 변경을 방지하기 위해,
객체의 변수는 객체의 메소드에 의해서만 변경될 수 있습니다.
이러한 유형의 변수를 개인 변수라고 합니다.

클래스는 모든 데이터를 캡슐화하므로 캡슐화의 예입니다.
즉, 멤버 함수, 변수 등입니다.

"""

# Python program to demonstrate private members
# private 멤버를 보여주는 Python 프로그램.

# Creating a Base class
# 기본 클래스 생성
class Base:
    def __init__(self):
        self.name = "Zokirkhon"
        self.__surname = "Kotibkhonov"

obj1 = Base();
print(obj1.name) 
#output: Zokirkhon
print(obj1.surname) 
#output: raise AttributeError: 'Base' object has no attribute 'surname'
print(obj1.__surname) 
#output: raise AttributeError: 'Base' object has no attribute '__surname'
