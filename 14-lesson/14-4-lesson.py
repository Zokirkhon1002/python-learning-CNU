# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:40:42 2021

@author: Zokirkhon
@topic: handling files and exceptions
"""

###1
# x,y = 2,0;
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("you can't divide by zero!")








###2
# x,y = 2,0;
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)


# x,y = 2,0;
# try:
#     print(x/y)
# except Exception as er:
#     print(er)







###3
# while True:
#     try:
#         n=int(input("enter a number: "));
#         break;
#     except ValueError:
#         print("you must enter an integer number!")
# print("an integer number is entered successfully!")






###4
# While opening a file, if the file doesn't exist, it will raise an exception.
# while True:
#     try:
#         f = input("enter a file name: ");
#         filename = open(f, "r");
#         print(filename.readlines());
#         break;
#     except IOError:
#         print(f"{f} file doesn't exist!")
#         print("please enter a valid file name!")



import turtle

m =turtle.Turtle()
m.speed(0)
v = turtle.Turtle()
v.speed(0)
turtle.bgcolor("white")

for i in range(200) :
        m.color("red")
        m.circle(i)
        m.forward(60)
        m.right(60)
        v.circle(i)
        v.forward(60)
        v.color("green")  
        v.right(60)





###5
# try:
#     f = open("testfile", "w");
#     f.write("testing write to file")
# except IOError:
#     print("Error: Couldn't find file or write data")
# else:
#     print("file is written successfully!")
#     f.close()
#     print("file is closed successfully!")








###6
# try:
#     fh=open("testfil", "r");
#     str = fh.readline();
#     print(str)
# except IOError:
#     print("Error: can't find file or read data")
# finally:
#     print("before file closed")
#     fh.close()
#     print("after file closed")