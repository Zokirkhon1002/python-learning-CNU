# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 05:58:49 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: Tuple, Dict, Str, Set and List

"""


# 1
# s1 = str("Hello")
# s2 = "World"

# print(s1)
# print(s2)

# s3 = "Hello" + "World"
# print(s3)

# lst1 = [x**x for x in range(5)]
# print(lst1)

# str1 = str(lst1)
# print(str1)
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# tup1 = (1,2,3)
# str2 = str(tup1)
# print(str2)


# 2
# word = "Python"
# print(word[0:2])
# print(word[2:4])
# print(word[4:])


# 3
# text = "Love will find a way"
# print("Love" in text)
# print("love" in text)

# input_text = input("Enter a text: ")
# if "c" in input_text:
#     print("There is a word 'c' in your text.")
# else:
#     print("There is not a word 'c' in your text.")


# 4
"""
Check if queue string comes first in dictionary

"""
# a = input("Enter word: ")
# b = input("Enter word: ")
# if (a < b):
#     print(f"{a} is before {b}")
# else:
#     print(f"{b} is before {a}")


# 5
# txt = "Never put off, till tomorrow that, what you can do today?"
# text = "Never put off till tomorrow that what you can do today?"

# print(txt.split(','))
# print(text.split())


# 6
# s = "abcdef"
# print(s.isalpha())
# print(s.isdigit())

# s1 = '12345'
# print(s1.isalpha())
# print(s1.isdigit())

# s2 = 'abc123de45f'
# print(s2.isalpha())
# print(s2.isdigit())


# 7
# str = "This is a pencil"
# print(str.startswith("This"))
# print(str.endswith("pencil"))
# print(str.find("is")) # First occurrence index (with word)
# print(str.rfind("is")) # First occurrence index (with each letter)
# print(str.count("i"))


# 8
# str = "This is a pencil"
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.replace('a','the'))


# 9
# White Space Character
# str1 = " Step by step, go ahead! "
# print(str1.rstrip())
# print(str1.lstrip())
# print(str1.strip())


# 10
"""
A palindrome is the same sentence whether read forward or double 1.
For example, "mom", "civic" and "dad" are example of palindromes.
Let's write a program that receive a string input 
from the user checks whether it is a palindrome.

input: Enter a text: dad 
output: it is a palindrome.

"""

# text = input("Enter a text: ")

# palindromes = ["mom", "civic","dad"]

# if text in palindromes:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")


# 11
"""
An acronym is a string created by collecting the first letters of each word, 
such as NATO(North Atlantic Treaty Organization).
Let's write a program that outputs the corresponding initials when the user inputs a sentence.

Input: Enter a text: North Atlantic Treaty Organization
Output: NATO

"""

# def initial(input):
#     result = '' # acronym
#     for word in input.split():
#         result += word[0]
#     return print(result.upper())

# text = input("Enter a text: ")
# initial(text)


# 12
"""
Number of characters, number of numbers in the phrase string.
Let's write a program that counts the number of spaces.

input: Enter a text: A picture is worth a thousand words.
output: {'digits':0,'spaces':6,'alphas':29}

"""

sentence = input("Enter a text: ")

table = {'digits': 0, 'spaces': 0, 'alphas': 0}

for i in sentence:
    if i.isalpha():
        table['alphas'] += 1
    if i.isdigit():
        table['digits'] += 1
    if i.isspace():
        table['spaces'] += 1

print(table)
