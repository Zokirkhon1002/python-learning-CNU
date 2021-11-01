# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:08:01 2021

@author: Kotibkhonovo Zokirkhon Zokhidkhon Ugli
student number: 180421
"""


###1
# class TV:
#     serialNumber=0
#     number=0
#     def __init__(self):
#         TV.serialNumber += 1;
#         self.number += 1;

# tv1 = TV();
# print(f"tv1.serialNumber: {tv1.serialNumber}") # tv1.serialNumber: 1
# print(f"tv1.number: {tv1.number}")             # tv1.number: 1
# print(f"TV.serialNumber: {TV.serialNumber}")   # TV.serialNumber: 1

# tv2 = TV();  
# print(f"tv2.serialNumber: {tv2.serialNumber}") # tv2.serialNumber: 2
# print(f"tv2.number: {tv2.number}")             # tv2.number: 1
# print(f"tv1.number: {tv1.number}")             # tv1.number: 1
# print(f"TV.serialNumber: {TV.serialNumber}")   # TV.serialNumber: 2

# tv3 = TV();
# print(f"tv3.serialNumber: {tv3.serialNumber}") # tv3.serialNumber: 3
# print(f"tv3.number: {tv3.number}")             # tv3.number: 1
# print(f"TV.serialNumber: {TV.serialNumber}")   # TV.serialNumber: 3






###2
# class ClassVar:
#     text_list = []
    
#     def add(self, text):
#         """Add some text to the list"""
#         self.text_list.append(text)
    
#     def print_textlist(self):
#         print(self.text_list)

# if __name__=="__main__":
#     obj1 = ClassVar();
#     obj1.add("Zokirkhon")
#     obj1.print_textlist()
    
#     obj2=ClassVar();
#     obj2.add("Sayfullokhon")
#     obj2.print_textlist()





###3
# class InstanceVar:
#     def __init__(self):
#         self.text_list = []
    
#     def print_text(self):
#         print(self.text_list)
        
#     def add(self, text):
#         """Add some text to the list"""
#         self.text_list.append(text)
    
#     def print_textlist(self):
#         print(self.text_list)

# if __name__=="__main__":
#     obj1 = InstanceVar();
#     obj1.add("Zokirkhon")
#     obj1.print_textlist()
    
#     obj2=Insobj1 = InstanceVar();
#     obj2.add("Sayfullokhon")
#     obj2.print_textlist()



###4
## class declaration part ##
# class Car:
#     color = ""
#     speed = 0
#     count = 0
    
#     def __init__(self):
#         self.length = 0
#         self.speed += 10
#         Car.count += 1

# ## Main code printing part ##
# print(f"Car.count: {Car.count}")
# print(f"Car.speed: {Car.speed}")
# # print(f"Car.length: {Car.length}")

# myCar1 = Car();
# print(f"1's current speed is {myCar1.speed}, There is {myCar1.count} car in total.")
# print(f"Car.count: {Car.count}")

# myCar2 = Car();
# myCar2.speed = 60
# print(f"2's current speed is {myCar2.speed}, There is {myCar2.count} car in total.")
# print(f"Car.count: {Car.count}")

# myCar3 = Car();
# myCar3.speed = 90
# print(f"3's current speed is {myCar3.speed}, There is {myCar3.count} car in total.")

# print(f"myCar1.count: {myCar1.count}")
# print(f"myCar2.count: {myCar2.count}")
# print(f"myCar3.count: {myCar3.count}")

# print(f"Car.count: {Car.count}")
# Car.count += 10
# print(f"Car.count: {Car.count}")





###5
# class Calculator:
    
#     @staticmethod
#     def plus(a, b):
#         """Return sum of two numbers"""
#         return a+b
    
#     @staticmethod
#     def minus(a,b):
#         return a-b
    
#     @staticmethod
#     def multiply(a,b):
#         return a*b
    
#     @staticmethod
#     def divide(a,b):
#         return a/b
    

# a = Calculator()
# print(a.plus(4,5))

# b = Calculator.plus(5,6)
# print(b)

# if __name__ == "__main__":
#     print(f"7 + 4 = {Calculator.plus(7,4)}")
#     print(f"7 - 4 = {Calculator.minus(7,4)}")
#     print(f"7 * 4 = {Calculator.multiply(7,4)}")
#     print(f"7 / 4 = {Calculator.divide(7,4)}")





###6
# class TestClass:
#     @classmethod
#     def print_TestClass(cls):
#         print(f"This is TestClass: {cls}")

# TestClass.print_TestClass()
# obj = TestClass()
# obj.print_TestClass()







###7
# class InstanceCounter:
#     count  = 0
#     def __init__(self):
#         InstanceCounter.count += 1
    
#     @classmethod
#     def print_instance_count(cls):
#         print(cls.count)

# if __name__ == "__main__":
#     a = InstanceCounter()
#     InstanceCounter.print_instance_count()
    
#     b = InstanceCounter()
#     InstanceCounter.print_instance_count()
    
#     c = InstanceCounter()
#     c.print_instance_count()





###8
# class CircleCalculator(object):
#     __PI = 3.14
    
#     # Class method to find area of a circle
#     @classmethod
#     def calculate_area(cls, radius):
#         area = cls.__PI * (radius**2)
#         return round(area,2)
    
#     # Class method to find circumference of a circle
#     @classmethod
#     def calculate_circumference(cls,radius):
#         circumference = 2*cls.__PI*radius
#         return round(circumference,2)

# if __name__ == '__main__':
#     print(f"Radius: 3, Area: {CircleCalculator.calculate_area(3)}")
#     print(f"Radius: 3, Circumference: {CircleCalculator.calculate_circumference(3)}")








###9
# difference between classmethod and staticmethod

# class Hello:
#     t="I gave Inherit"
    
#     @classmethod
#     def calc(cls):
#         return cls.t 
    
#     @staticmethod
#     def calc_static():
#         return Hello.t # It's related to Hello Class only.

# class Hello_2(Hello):
#     t = "I recieved Inherit"

# print(Hello_2.calc()) # I recieved Inherit
# print(Hello_2.calc_static()) # I gave Inherit

# ##output:
# # I recieved Inherit
# # I gave Inherit





###10
class Person:
    default = "Father"
    def __init__(self):
        self.data = self.default
    
    @classmethod
    def class_person(cls):
        return cls.default
    
    @staticmethod
    def static_person():
        return Person.default

class What_Person(Person):
    default = "Mother"

person1 = What_Person.class_person()
person2 = What_Person.static_person()
print(person1) # Mother
print(person2) # Father
