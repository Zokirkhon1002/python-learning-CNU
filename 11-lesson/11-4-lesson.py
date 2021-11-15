# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:44:06 2021

@author: Zokirkhon
Topic: Functions
"""





### 1
from datetime import date

# def print_date():
#     print(date.today());
#     print("Hello World!")

# print_date();








### 2
# def print_hi():
#     print("Hello Python");

# def dec01(func):
#     def newfunc():
#         print(F"Today: {date.today()}")
#         func();
#     return newfunc;
# result = dec01(print_hi);
# result()








### 3
# def deco3(func):
#     def new_func():
#         print("Today:", date.today())
#         func();
#     return new_func;

# def deco4(func):
#     def new_func():
#         print("Python V.3.10.0")
#         func();
#     return new_func;

# @deco3
# @deco4
# def print_hi5():
#     print("Double Decorator");

# print_hi5();





### 4
# def deco5(func):
#     def new_func(name, age):
#         print(f"Today: {date.today()}")
#         func(name, age)
#     return new_func


# @deco5
# def print_hi(name, age):
#     print(f"Hi {name}, you are {age} years old.")


# print_hi("Zokirkhon", "21")


###4.1
def deco5(func):
    def new_func(name, age):
        print(f"Today: {date.today()}")
        func(name, age)
    return new_func


def print_hi(name, age):
    print(f"Hi {name}, you are {age} years old.")

print_hi2 = deco5(print_hi)
print_hi2("Zokirkhon", "21")
