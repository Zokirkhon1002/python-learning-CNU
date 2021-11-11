# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:26:34 2021

@author: Zokirkhon Kotibkhonov
topic: Inheritence, Polymorphism(overriding) and encapsulation, information hiding

"""


###1
### This is a class representing general means of transportation;
# class Vehicle:
#     def __init__(self,make,model,color,price):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.price = price
    
#     def setMake(self,make):
#         self.make = make
#     def getMake(self):
#         return self.make
    
#     # Returns information about the vehicle as a summary as a string.
#     def getDesc(self):
#         return (f"vehicle: {str(self.make)}"
#                 f"{self.model}"
#                 f"{self.color}"
#                 f"{self.price}")

# class Truck(Vehicle):
#     def __init__(self,make,model,color,price,payload):
#         super().__init__(make,model,color,price)
#         self.payload = payload
    
#     def setPayLoad(self,payload):
#         self.payload = payload
    
#     def getPayload(self):
#         return self.payload

# def main():
#     myTruck = Truck("Ford ","F-150 ","blue ",10000,2000)
#     myTruck.setMake("Toyota")
#     myTruck.setPayLoad(3000)
#     print(myTruck.getDesc())

# main();





###2
# class Animal:
#     def __init__(self,name=""):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")
# class Dog(Animal):
#     def __init__(self,name):
#         super().__init__(name)
#     def eat(self):
#         print(f"{self.name} is eating")

# d = Dog("Bobby")
# print(d.name)
# d.eat();









###3
# class Account():
#     def __init__(self,money):
#         self.balance = money
    
#     def withdraw(self,amount):
#         self.balance -= amount

# class Blue_Account(Account):
#     def __init__(self,name,money):
#         Account.__init__(self,money)
#         self.name = name
#     def withdraw(self,money):
#         self.balance += money

# my_account=Blue_Account("Zokirkhon",100)
# print(my_account.balance)
# my_account.withdraw(50)
# print(my_account.balance)






###4
##4.1
# class A():
#     def method(self):
#         print("A's Method")

# class B(A):
#     def method(self):
#         print("B's Method")

# class C(B):
#     def method(self):
#         B.method(self)
#         super().method()
# test = C()
# test.method()


##4.2
# class A():
#     def method(self):
#         print("A's Method")

# class B(A):
#     def method(self):
#         print("B's Method")

# class C(B):
#     def method(self):
#         A.method(self)
#         super().method()
# test = C()
# test.method()







###5
# class A:
#     def method(self):
#         print("A's Method")

# class B(A):
#     def method(self):
#         print("B's Method")

# class C(A):
#     def method(self):
#         pass

# class D(B,C):
#     pass

# obj = D();
# obj.method()









###6
# class Car:
#     def __init__(self, speed):
#         self.speed = speed
#     def setSpeed(self, speed):
#         self.speed = speed
#     def getDescription(self):
#         return f"Vihecle: {self.speed} km/h"

# class SportsCar(Car):
#     def __init__(self,speed,turbo):
#         super().__init__(speed)
#         self.turbo = turbo
#     def setTurbo(self,turbo):
#         self.turbo = turbo

# obj = SportsCar(100,True)
# print(obj.getDescription())
# obj.setTurbo(False)
# print(obj.getDescription())







###7
## let's write a programm As an example of sphere ingeritence, create a Shape class,
## (x coordinate, y coordinate, area(), perimeter()) that represents
## a general polygon, and inherit it and inherit a Rectangele class
## that represents a rectangle, (x coordinate, y coordinate, horizontal length, vertical length, area(), perimeter())

# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         print("can not compute")
#     def perimeter(self):
#         print("can not compute")

# class Rectangle(Shape):
#     def __init__(self,x,y,w,h):
#         super().__init__(x,y)
#         self.w = w
#         self.h = h
    
#     def area(self):
#         return self.w*self.h
#     def perimeter(self):
#         return 2*(self.w+self.h)

# r = Rectangle(0,0,100,200)

# print(f"Area of Rectangle: {r.area()}")
# print(f"Perimet of Rectangle: {r.perimeter()}")







###8
## Let's write a Person class that represents an ordinary person.
## Inherit the Person class and define the class StLJdent representing the student and 
## the class Teacher representing the teacher.

# class Person:
#     def __init__(self,name,number):
#         self.name = name
#         self.number = number

# class Student(Person):
#     UNDERGRADUATE = 0   #constant
#     POSTGRADUATE = 1    #constant
    
#     def __init__(self,name,number,studentType):
#         super().__init__(name,number)
#         self.studentType = studentType
#         self.gpa=0
#         self.classess = []
    
#     def enrollCourse(self,course):
#         self.classess.append(course)
    
#     def __str__(self):
#         return f"Name: {self.name}, Number: {self.number},  Classes: {self.classess}, Graduation: {self.gpa}";
# class Teacher(Person):
#     def __init__(self,name,number):
#         super().__init__(name,number)
#         self.courses = []
#         self.salary = 3_000_000
    
#     def assignTeaching(self,course):
#         self.courses.append(course)
    
#     def __str__(self):
#         return f"Name: {self.name}, Number: {self.number},  Courses: {self.courses}, Salary: {self.salary}";

# zokirkhon = Student("Zokirkhon","123456",Student.UNDERGRADUATE)
# zokirkhon.enrollCourse("Data Structure")
# print(zokirkhon)

# kim = Teacher("KimCholsu","12345")
# kim.assignTeaching("Python")
# print(kim)





###9
# class BankAccount:
#     def __init__(self,name,number,balance):
#         self.balance = balance
#         self.name = name
#         self.number = number
    
#     def withdraw(self,amount):
#         self.balance -= amount
#         return self.balance
    
#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance

# class SavingAccount(BankAccount):
#     def __init__(self,name,number,balance,interest_rate):
#         super().__init__(name,number,balance)
#         self.interest_rate = interest_rate
    
#     def set_interest_rate(self,interest_rate):
#         self.interest_rate = interest_rate
    
#     def get_interest_rate(self):
#         return self.interest_rate
    
#     def add_interest(self):
#         self.balance += self.balance*self.interest_rate

# class CheckingAccount(BankAccount):
#     def __init__(self,name,number,balance):
#         super().__init__(name,number,balance)
#         self.withdraw_charge = 10000 #check issuance fee
    
#     def withdraw(self,amount):
#         return BankAccount.withdraw(self,amount+self.withdraw_charge)

# a1 = SavingAccount("Zokirkhon","123456",2_000_000,0.03)
# a1.add_interest()
# print(f"Gold balance for savings: {a1.balance}")

# a2 = CheckingAccount("Kim Chol Su","123456",3_000_000)
# a2.withdraw(1_000_000)
# print(f"Gold balance for checking: {a2.balance}")








###10
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def getSalary(self):
#         return self.salary

# class Manager(Employee):
#     def __init__(self,name,salary,bonus):
#         super().__init__(name,salary)
#         self.bonus = bonus
    
#     def getSalary(self):
#         salary = super().getSalary()
#         return salary + self.bonus
    
#     def __repr__(self):
#         return f"name: {self.name}, salary: {self.getSalary()} won, bonus: {self.bonus}"

# kim = Manager("KimCholSu",3_000_000,1_000_000)
# print(kim)
