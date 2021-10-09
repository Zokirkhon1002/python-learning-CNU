# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:38:43 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""
import math;
import random;


# # #1
# def sphereVolume(r):
#     """Return the volume of a sphere"""
#     v=(4/3)*math.pi*r**3
#     return v

# r = float(input("Please enter a radius of sphere:\n>>> "))
# print(sphereVolume(r))








# # #2
# def genPass():
#     alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
#     password = ""
    
#     for i in range(6):
#         index = random.randrange(len(alphabet));
#         password += alphabet[index]
#     return password

# print(genPass())
# print(genPass())
# print(genPass())








# # #3
# def print_info(name,age):
#     """Return the informations of person"""
#     print("="*20)
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print("="*20)
#     return
# print_info("Zokirkhon",23)
# return_value = print_info("Sayfullokhon",23)
# print(return_value)









# # #4
# def greet(name,msg="are you ok?"):
#     """Return the greeting for argument"""
#     print(f"Hello, {name}, {msg}")
# greet("Zokirkhon")
# greet("Zokirkhon", "Good Morning")








# # #5
# def calc(x,y,z):
#     return x+y+z;
# print(calc(10,20,30))
# print(calc(x=10,y=20,z=30))
# print(calc(y=20,x=10,z=30))






# # #6
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# r1 = mul(a=20,b=30)
# r2 = add(a=10, b=r1)
# print(r2)








# # #7
def printOptions():
    print("\n 'c' Celsius to Fahrenheit")
    print(" 'f' Fahrenheit to Celsius")
    print(" 'q' End")
def C2F(c_temp):
    return 9.0/5.0*c_temp+32
def F2C(f_temp):
    return (f_temp - 32.0)*5.0/9.0


printOptions()
choice = input("Please select from the menu: ")
while choice != "q":
    if choice == "c":
        temp = float(input("Celsius Temprature: "))
        print(f"\nFahrenheit Temprature: {C2F(temp)}")
    elif choice == 'f':
        temp = float(input("Fahrenheit Temprature: "))
        print(f"\nCelsius Temprature: {F2C(temp)}")
    printOptions()
    choice = input("Please select from the menu: ")






































