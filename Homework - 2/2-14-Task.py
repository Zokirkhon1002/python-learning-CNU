# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:16:38 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Let's write a program that calculates (1+2+3+...+n) by adding 
# from 1 to the number n entered by user. The for statement is a
# simple way to get the sum.


# # # 1-solution.
n = int(input("Enter an integer number: "))
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)



# # # 2-solution

x = int(input("Enter an integer number: "))

result = n*(n/2) + (n/2);

print(int(result))




