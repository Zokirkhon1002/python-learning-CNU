# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:02:29 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""
# Task:
# Let's write and execute a program that prints out the gades by
# extending the students' grades. A grade of 90 pr higher is an A grade,
# a score of 80 or higher and les than 90 is a B grade,
# if the score is 70 or more and less than 80, the grade of C, and outside
# will be decided.


grade = float(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is: A")
elif grade >=80 and grade < 90:
    print("Your grade is: B")
elif grade >=70 and grade < 80:
    print("Your grade is: C")
elif grade >=60 and grade < 70:
    print("Your grade is: D")
else:
    print("Your grade is: F \nYou have failed")

