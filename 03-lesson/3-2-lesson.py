# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:43:14 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""



# #1
# a = 0xFF
# b = 0o77
# c = 0b1111

# print(a,b,c)



# #2
# print(10 and 6) #1010 and 0110
# print(10 & 6) #1010 & 0110
# print(1 & 1)  #0001 and 0001
# print(1 & 0) #0001 and 0000
# print(0 & 0) #0000 and 0000
# print(0 & 1) #0001 and 0001
# print(0b1111 & 0b1010) # 15 & 10



# #3
# print(1|1)
# print(1|0)
# print(0|1)
# print(0|1)
# print(0b1110|0b1010)
# print(10|6)
# print(10|4)



# #4
# print(1^1)
# print(1^0)
# print(0^1)
# print(0^0)
# print(0b1110^0b1010)



# #5
# print(~0)
# print(~1)
# print(~2)
# print(~3)
# print(~-1)
# print(~-2)
# print(~-3)
# print(~0b1010)
# print(~0b11110000)




# #6
# a = 10
# print(a<<1,a<<2,a<<3,a<<4)





# #7
# a = 10
# print(a>>1,a>>2,a>>3,a>>4)




# #8
# lessons = int(input("How many lessons have you studeid?\n>>> "))
# gpas = []
# summary = 0

# for n in range(lessons):
#     gpas.append(float(input(f"please enter your {n+1}-lesson's grade\n>>> ")))
    
# print(f"Your grades {gpas}")

# if not len(gpas)==0:
#     for each in gpas:
#         summary += each
#         result = summary / len(gpas)
#     if result>=90:
#         last_result = "Your grade is A"
#     elif result>=80:
#             last_result = "Your grade is B"
#     elif result>=70:
#         last_result = "Your grade is C"
#     elif result>=60:
#         last_result = "Your grade is D"
#     else:
#         last_result = "Your grade is F"
# else:
#     print("You don't have GPA")
# print(last_result)




# #9
# n=int(input("Enter an integer:\n>>> "))
# if n<0:
#     print("Integer entered is negative")
# elif n==0:
#     print("Integer entered is 0")
# else:
#     print("Integer entered is positive")




# #10
# apple_quality = input("Please enter quality of apple:(fresh/not)\n>>> ").lower()
# apple_price = int(input("Please enter price of apple:\n>>> "))
# if apple_quality == 'fresh':
#     if apple_price < 1000:
#         print("I will buy 10 apples")
#     else:
#         print("I will buy 5 apples")
# else:
#     print("I will not buy apples")





# #11
# n=int(input("Enter an integer:\n>>> "))
# if n>=0:
#     if n==0:
#         print("Integer entered is 0")
#     else:
#         print("Integer entered is positive")
# else:
#     print("Integer entered is negative")





# #12
# user_list = ['khan', 'umar', 'ali', 'muhammad']
# password_list = ['1234', '42321', '5678', '8765']

# name = input("Please enter your ID:\n>>> ").lower()
# if name in user_list:
#     password = input("please enter your password:\n>>> ")
#     if password in password_list:
#         print("Welcome!")
#     else:
#         print("Invalid password")
# else:
#     print("Unknown user")




# #13
# allMonths = ['january','february','march','april','may','june','july',
#              'august','september','october','november','december']

# months31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
# months30 = ['april', 'june', 'september', 'november']

# month_n31 = [1, 3, 5, 7, 8, 10, 12]
# month_n30 = [4, 6, 9, 11]

# result = ''
# month = input("Enter month's name or month's number:\n>>> ")
# if len(month)<=2:
#     month = int(month)
#     if month == 2:
#         result = "Febrary has 28/29 days"
#     elif month in month_n31:
#         result = f"{allMonths[month-1].title()} has 31 days"
#     elif month in month_n30:
#         result = f"{allMonths[month-1].title()} has 30 days"
# else:
#     month = str(month).lower()
#     if month == 'february':
#         result = f"{month.title()} has 28/29 days"
#     elif month in months31:
#         result = f"{month.title()} has 31 days"
#     elif month in months30:
#         result = f"{month.title()} has 30 days"

# print(result)





# #14
# year = int(input("Enter a year\n>>> "))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year}-year is leap year")
# else:
#     print(f"{year}-year is not leap year")





# #15
# import math

# a=float(input("a= "))
# b=float(input("b= "))
# c=float(input("c= "))

# d = b*b-4*a*c

# if a==0:
#     print(f"x= {-c/b}")
# if d==0:
#     print(f"x= {-b/(2.0*a)}")
# elif d>0:
#     print(f"x1= {(-b+math.sqrt(d))/(2.0*a)}")
#     print(f"x2= {(-b-math.sqrt(d))/(2.0*a)}")
# else:
#     print("Real root does not exist.")






# #16
# from random import randint

# answer = randint(1,100)
# guess = int(input("Welcome to Random game.\nGuess the number:\n>>> "))
# if guess >= answer:
#     if guess == answer:
#         print("User has won the game")
#     else:
#         print("Too Big")
# else:
#     print("Too small")
# print("Game is over.")




# #17
# import random

# player = input("Choose one of ('scissor', 'rock', 'paper'):\n>>> ").lower()

# random_number = random.randint(0,2)

# if random_number == 0:
#     computer = "scissor";
# elif random_number == 1:
#     computer = "rock";
# else:
#     computer = "paper"
# print(f"User: {player}, Computer: {computer}")

# comp = computer == 'rock' and player == 'scissor' or computer == 'scissor' and player == 'paper' or computer == 'paper' and player == 'rock';
# user = computer == 'rock' and player == 'paper' or computer == 'scissor' and player == 'rock' or computer == 'paper' and player == 'scissor';

# if computer == player:
#     print("Draw!")
# elif comp:
#     print("Computer won!")
# elif user:
#     print("User won!")






























































