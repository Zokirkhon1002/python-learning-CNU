# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:35:15 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""


# #1
# i = 0
# while i<5:
#     print("Welcome")
#     i+=1
# print("Repeat has ended")




# #2
# i = 0
# while i<10:
#     print(i,end=" ")
#     i+=1
# print("Repeat has ended")





# #3
# n = 1
# sum = 0
# while n<=10:
#     sum += n
#     n += 1 
# print(f"all: {sum}")






# #4
# n = 1
# sum = 1
# while n<=10:
#     sum *= n
#     n += 1 
# print(f"all: {sum}")





# #5
# n = 1
# while n<=9:
#     print("3*%d=%d"%(n,3*n))
#     n += 1 







# #6
# summary = 0
# number = 1

# while number <= 100:
#     if number%3==0:
#         summary+=number
#     number += 1
# print("The sum of multiples of 3 between 1 and 100 is %d"%summary)






# #7
# nums = 12345
# sums = 0
# while nums>0:
#     digits = nums % 10
#     print(digits)
#     sums += digits
#     nums //= 10
# print("The sum of digits is %d"%sums)






# #8
# n=0
# sums=0
# score=0

# print("In order to exit, enter negative number")
# while score>=0:
#     score = int(input("Enter your grade:\n>>> "))
#     if score>=0:
#         sums+=score
#         n+=1
# if n>0:
#     average = sums /n
# print(f"The grade average is {average}")







# #9
# # Interesting game
import random
tries = 0 
n = random.randint(1,100)
print("Guess a number between 1 and 100")

while tries<10:
    guess = int(input("Please enter a number\n>>> "))
    tries+=1
    if guess < n:
        print("too small!")
    elif guess > n:
        print("too big!")
    else:
        break
if guess == n:
    print(f"Congratulation. number of attemps: {tries}")
else:
    print(f"The answer is {n}")






# #10
# a,b,c,d,e = 1,2,3,4,5
# print(a,b,c,sep="-",end="::")
# print(d,e)
# print(a,b,c,sep="-")
# print(d,e)







# #11
# # print(("*"*10 + '\n')*5)

# for x in range(5):
#     for y in range(10):
#         print("*",end="")
#     print("")




# #12
# for a in range(1,101,1):
#     for b in range(1,101,1):
#         for c in range(1,101,1):
#             if((a*a+b*b)==c*c):
#                 print(a,b,c)



# #13
# fruit = "apple"
# for letter in fruit:
#     print(letter, end=" ")





# #14 
# s = input("Enter a string:\n>>> ")
# vowels = "aAeEiIoOuU"
# result = ""
# for letter in s:
#     if letter not in vowels:
#         result += letter
# print(result)






# #15
# original = input("Please enter a word:\n>>> ")
# l_word = original.lower()
# result_vowels = 0
# result_consonants = 0

# if len(original) > 0 and original.isalpha():
#     for each_letter in l_word:
#         if each_letter in 'aeiou':
#             result_vowels +=1
#         else:
#             result_consonants +=1

# print(f"Vowels: {result_vowels}")
# print(f"Consonants: {result_consonants}")






# #16
# input_string = input("Please write some words:\n>>> ")
# alphas,digits,spaces = 0,0,0

# for c in input_string:
#     if c.isalpha():
#         alphas +=1
#     if c.isdigit():
#         digits +=1
#     if c.isspace():
#         spaces +=1
    
# print(f"Number of alphabets: {alphas}"
#       f"\nNumber of digits: {digits}"
#       f"\nNumber of spaces: {spaces}")








# #17
# str1 = "Zokirkhon Kotibkhonov"
# str2 = "ZokirkhonKotibkhonov"
# print(str1.isalpha())
# print(str2.isalpha())








# #18
# raw = input("Please enter number of your Bankbook:\n>>> ")
# result = ""

# for c in raw:
#     if c != "-":
#         result +=c
# print(result)









































