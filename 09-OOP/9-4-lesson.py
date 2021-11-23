# -*- coding: utf-8 -*-
"""
Created on Mon Nov 01 19:46:33 2021

@author: Kotibkhonovo Zokirkhon Zokhidkhon Ugli
student number: 180421
"""



###1
# from abc import *

# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
    
#     @abstractmethod
#     def go_to_school(self):
#         pass

# class Student(StudentBase):
#     def study(self):
#         print("Study, Study.")


# zokirkhon = Student()
# zokirkhon.study()

## output
## Traceback (most recent call last):  
## File "D:\Coding Class\Self study from Videos\Python programming\Chonnam National University\09-OOP\9-4-lesson.py", 
## line 29, in <module> zokirkhon = Student()
## TypeError: Can't instantiate abstract class Student with abstract method go_to_school






###2
# from abc import *

# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
    
#     @abstractmethod
#     def go_to_school(self):
#         pass

# class Student(StudentBase):
#     def study(self):
#         print("Study, Study.")
#     def go_to_school(self):
#         print("Go to school, Go to school.")


# zokirkhon = Student()
# zokirkhon.study()
# zokirkhon.go_to_school()

## Output
## Study, Study.
## Go to school, Go to school.





###3
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def __eq__(self, other):
#         return self.radius == other.radius

# c1= Circle(10)
# x = int(input("Enter radius: "))
# c2= Circle(x)
# if c1 == c2:
#     print("They are equal")

## Output
## They are equal





###4
# class Vector2D:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         print(f"__init__(): {x,y}")
    
#     def __add__(self,other):
#         print("__add__()")
#         return Vector2D(self.x + other.x, self.y + other.y)
    
#     def __sub__(self,other):
#         print("__sub__()")
#         return Vector2D(self.x - other.x, self.y - other.y)
    
#     def __eq__(self,other):
#         print("__eq__()")
#         return self.x == other.x and self.y == other.y
    
#     def __str__(self):
#         print("__str__()")
#         return f"{self.x} {self.y}"

# u = Vector2D(0,1)
# v = Vector2D(1,0)
# w = Vector2D(1,1)
# a = u + v;
# print(a)
# print(v)





###5
# class Bag:
#     def __init__(self):
#         self.data = []
    
#     def add(self,x):
#         self.data.append(x);
#     def add2(self,x):
#         self.add(x)
#         self.add(x)
#         print(self.data)

# bag = Bag()
# bag.add2(5)
# bag.add2(7)

