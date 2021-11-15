
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  12 01:56:34 2021

@author: Zokirkhon Kotibkhonov
topic: Classes and Objects
"""




###1
# list = [1,2,3]
# print(len(list))
# s="This is a sentnces"
# print(len(s))
# d={'aaa':1,'bbb':2}
# print(len(d))







###2
# class Animal:
#     def __init__(self,name):
#         self.name = name;
#     def speak(self):
#         return "Can not be understandable"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# animalList = [Dog("dog1"),Dog("dog2"),Cat("cat1")]
# for a in animalList:
#     print(f"{a.name} : {a.speak()}")





###3
# class Vehicle:
#     def __init__(self,name):
#         self.name = name;
    
#     def drive(self):
#         raise NotImplementedError("Subclass must implement abstract method")
    
#     def stop(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Car(Vehicle):
#     def drive(self):
#         return "Car is moving"
#     def stop(self):
#         return "Car is stopped"

# class Truck(Vehicle):
#     def drive(self):
#         return "Truck is moving"
#     def stop(self):
#         return "Truck is stopped"

# cars = [Truck("truck1"),Truck("truck2"),Car("car1")]

# for c in cars:
#     print(f"{c.name} : {c.drive()}")
#     print(f"{c.name} : {c.stop()}")







###4
# class Book:
#     def __init__(self,title,isbn):
#         self.__title = title
#         self.__isbn = isbn
#     def __repr__(self):
#         return f"ISBN: {self.__isbn}; TITLE: {self.__title}"
# book = Book("The Python Tutorial","0123456")
# print(book)







###5
# class MyTime:
#     def __init__(self,hour,minute,second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#     def __str__(self):
#         return f"{self.hour}:{self.minute}:{self.second}"

# time=MyTime(20,25)
# print(time)








###6
# class Animal:
#     pass
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name

# class Person(object):
#     def __init__(self,name):
#         self.name = name
#         self.pet = None;

# dog1 = Dog("dog1")
# person1 = Person("person1")
# person1.pet = dog1
# print(person1.pet.name)
# print(person1.name)








###7
# Write the Card class that represents the old cards and 
# the Deck class that has 52 Card objects. Implement the str() method
# for each class to output the cards in the deck as follows
class Card:
    suitNames = ["Clubs","Diamonds","Hearts","Spades"]
    rankNames = ["None","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{Card.suitNames[self.suit]} {Card.rankNames[self.rank]}"
class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()
print(deck)