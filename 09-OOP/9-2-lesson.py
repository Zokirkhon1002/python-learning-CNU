# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 00:00:55 2021

@author: Kotibkhonovo Zokirkhon Zokhidkhon Ugli
student number: 180421
"""

### 1
# class Student:
#     def __init__(self, name=None, age=0):
#         self.name = name
#         self.age = age
#     def __repr__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# s1 = Student("Zokirkhon",23)
# print(s1)
# s1.age = 24
# s1.name = "Abdulloh"
# print(s1)


### 2
# class Student:
#     def __init__(self, name=None, age=0):
#         self.__name = name
#         self.__age = age

# obj = Student()
# print(obj.__age)  # AttributeError: 'Student' object has no attribute '__age'


### 3
# class Student:
#     def __init__(self, name=None, age=0):
#         self.__name = name
#         self.__age = age

#     def getName(self):
#         return self.__name

#     def getAge(self):
#         return self.__age

#     def setName(self, name):
#         self.__name = name

#     def setAge(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             self.__age = 0

# obj = Student("Zokirkhon",23)
# print(obj.getName())
# print(obj.getAge())


### 4
# let's also mark the class as the circle. A circle has a radius.
# let's also define a method to calculate the area and circumference of a circle.
# It also writes setter and accessor methods.

# import math
# class Circle:
#     def __init__(self, radius=1.0):
#         self.__radius = radius

#     def setRadius(self, radius):
#         self.__radius = radius

#     def getRadius(self):
#         return self.__radius

#     def calcArea(self):
#         return math.pi * self.__radius ** 2

#     def calcCircumference(self):
#         circumference =  2.0 * math.pi * self.__radius
#         return circumference;

# c1 = Circle(10)

# print(f"Radius of Circle: {c1.getRadius()}")
# print(f"Area of Circle: {c1.calcArea()}")
# print(f"Circumference of Circle: {c1.calcCircumference()}")


### 5
# We can deposit and withdraw money into our bank account.
# Let's model a bank account as a class.
# A bank account has only the current balance as an instance variable.
# Assume only the constructor and withdrawal
# method widthdraw() and the savings method deposit().

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawing {amount} from your account.")
#             return self.__balance;
#         else:
#             print("Your don't have enough balance to withdraw")

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Depositing {amount} into your account.")
#         return self.__balance;

# a = BankAccount()
# print(a.deposit(100))
# print(a.withdraw(20))


### 6
# Define the old cat as a class. A cat has a name and age attributes.
# class Cat:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def setName(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     def setAge(self, age):
#         self.__age = age

#     def getAge(self):
#         return self.__age

# missy = Cat("Missy", 3)
# lucky = Cat("Lucky", 5)

# print(missy.getName(), missy.getAge())
# print(lucky.getName(), lucky.getAge())


### 7
# Let's write a Box class that reperesents a sphere box.
# Box class has instance variables representing width, height, and length.

# class Box:
#     def __init__(self, width, length, height):
#         self.__width = width
#         self.__length = length
#         self.__height = height

#     def setWidth(self, width):
#         self.__width = width

#     def setLength(self, length):
#         self.__length = length

#     def setHeight(self, height):
#         self.__height = height

#     def getVolume(self):
#         return self.__width * self.__length * self.__height;

#     def __str__(self):
#         return f"Box: {self.__width}, {self.__length}, {self.__height}"

# box = Box(100,100,100)
# print(box)
# print(box.getVolume())


### 8
# Let's define a class that reperesents the queue car.
# For example, for a car object,
# the property is color, current speed, and current gear, etc.
# The operation of the car  may include shifting, accelerating, and decelerating a Kia.
# Let's implement it by selecting only the properties and actions shown in the figure below.

# class Car:
#     def __init__(self, color="white", speed=0, gear=1):
#         self.__color = color
#         self.__speed = speed
#         self.__gear = gear

#     def setSpeed(self, speed):
#         self.__speed = speed

#     def setGear(self, gear):
#         self.__gear = gear

#     def setColor(self, color):
#         self.__color = color

#     def __str__(self):
#         return f"Car: {self.__speed}, {self.__gear}, {self.__color}"

# myCar = Car()
# myCar.setSpeed(100)
# myCar.setGear(3)
# print(myCar)


### 9
# What if an old object is passed to a function to change the object?
# Depends on type of object.
# If immutable objects such as numbers or strings are passed in, those
# objects are immutable.
# Functions can mutate objects when user-written objects are passed.


# # If the old object is passed, the function can change the object.
# # Define a rectangle as a class.
# class Rectangle:
#     def __init__(self, side=0):
#         self.side = side

#     def getArea(self):
#         return self.side * self.side

# # Recieve a rectangle object and the number of iterations, and print
# # the area of while increasing the side.
# def printAreas(rect, iterations):
#     while iterations > 0:
#         print(f"{rect.side} \t {rect.getArea()}")
#         rect.side += 1
#         iterations -= 1

# # By calling the queue printAreas(), we check whether the contents of the object change.

# myRect = Rectangle()
# count = 5
# printAreas(myRect, count)
# print(f"Rectangle side: {myRect.side}")
# print(f"Rectangle repeat: {count}")