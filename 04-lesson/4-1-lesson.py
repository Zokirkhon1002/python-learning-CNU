# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:31:00 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""


# #1
# for x in range(5):
#     print("Welcome")

# print("Welcome\n"*5)







# #2
# for name in ['Khan', 'Umar', 'Zokirkhon', 'Ali']:
#     print(f"Hello, {name}")








# #3
# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x, end=' ')
    # print(x, sep=',')
    # print(x, end='-')
    # print(x, flush=True)








# #4
# sum = 0
# for x in range(10):
#     sum+=x
# print(sum)



# sum = 0
# for x in range(0,10):
#     sum+=x
# print(sum)







# #5
# for letter in 'abcdef':
#     print(letter, end=" ")

# print('\n',1,2,3,4,5,sep='/',end=':end')






# #6
# number = int(input("Please enter a number:\n>>> "))
# sum = 0
# for x in range(1,number+1):
#     sum+=x

# print(sum)








# #7
# # Finding the factorial using iteration
# fact = 1.0
# number = int(input("Please enter an integer:\n>>> "))
# for i in range(1,number+1):
#     fact*=i
# print(f"{number} !is, {fact}")







# #8
# for x in range(0,101,10):
#     c = (x - 32)*5/9
#     print(f"{x} => {round(c,2)}")







# #9
# #Star
# import turtle
# star = turtle.Turtle();

# for i in range (5):
#     star.forward(200)
#     star.right(576)







# #10
# #Polygon
# import turtle
# polygon = turtle.Turtle();

# n_sides = 6
# side_length = 100
# angle = 360.0 / n_sides

# for i in range (n_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)








# #11
# import turtle
# t = turtle
# n = int(input("Please enter an integer:\n>>> "))
# for i in range(n):
#     t.left(20)
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)






# #12
# import math
# import turtle

# t=turtle.Turtle()
# t.pendown()
# for x in range(360):
#     y=math.sin(math.radians(x))
#     scaledX = x
#     scaledY = y*100
#     t.goto(scaledX,scaledY)
# t.penup()



















































