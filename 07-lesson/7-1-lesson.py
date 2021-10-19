# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:24:38 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: Tuple, Dict, Str, Set and List
"""



###1
# colors = ("red","green","blue")
# print(colors)
# numbers = (1,2,3)
# print(numbers)




###2
# a = 'kkc'
# print(tuple(a))
# print((1,2,3))
# print(tuple([5,6,7]))
# print(tuple((1,2,3,4)))
# print(tuple(1,2)) # typeError






###3
# tupl = 1,2,3
# print(tupl)






###4
# a = 'kkc'
# print(a)
# print([a])
# print((a))
# print([a,])
# print((a,))

# print("\n"*3)


# z = ('abc')
# print(z)
# z = ('abc',)
# print(z)
# print(tuple(a))
# print(tuple((a)))
# print(tuple([a]))

# print("\n"*3)


# print(tuple('kkc'))
# print(tuple(('kkc')))
# print(tuple(['kkc']))
# print(list(a))
# print(list([a]))
# print(list((a)))
# print(list((a,)))
# print(list([a,]))






###5
# numbers = (1,2,3,4,5)
# colors = ("red","green","blue")
# t = numbers + colors
# print(t)





###6
# tup4 = ([1,2,3,4,5])
# print(tup4)
# print(type(tup4))

# tup45 = (1,2,3,4,5)
# print(tup45)
# print(type(tup45))







###7
# t=(1,2,'hello')
# u=t,(5,6,7)
# print(u)

# tup7 = 1,2,3
# print(tup7)
# tup8 = tup7,'kkc',123
# print(tup8)
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)






###8
# y='zokirkhon'
# x=tuple(y)
# print(x)
# print(x[5])
# print(x[5:9])







###9
# tup=(1,2,(3,4,5),[6,7,8],'kkc')
# print(tup)
# tup[3][1] = 1000
# print(tup)






###10
# tup45 = (1,2,3,4,5,6)
# print(max(tup45))
# print(min(tup45))
# print(len(tup45))






###11
# t1 = (1,2,3,4,5,6)
# colors = ("green", "red", "blue")
# t = t1, colors
# print(t)

# t2 = (10,20)
# t3 = t1+t2
# print(t3)

# t4 = t3 + colors
# print(t4)





###12
# list = [0,1,2,3,4,5,6,7,8,9,10]
# print(list[1:9:1])
# print(list[1:9])
# print(list[1:9:2])
# print(list[9:1:-2])





###13
# t = ('apple', 'strawberry','banana')
# print(t[1])
# print(t[-2])
# print(t[1:])
# print(t[:1])
# print(t[0:2])
# print(t[1][2])








###14
# student = ("Zokirkhon",23,'International Trade')
# name,age,major = student
# print(name)
# print(age)
# print(major)

# (name1, age1, major1)=student
# print(name1)
# print(age1)
# print(major1)






###15
# a = 10
# b = 20
# c = a
# a = 20
# b = c
# print(a)
# print(b)


# a = 10
# b = 20
# (a,b) = (b,a)
# print(a)
# print(b)





###16
import math

def calculate_Circle(radius):
    """A function that simultaneously returns the area and circumference of
       of a circle of radius."""
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return (area, circum)

radius = float(input("Enter the radius of the circle: "))
(area, circum) = calculate_Circle(radius)

print(f"The area of circle is: {area}."
      f"\nAnd Circumference of the circle is: {circum}")





































