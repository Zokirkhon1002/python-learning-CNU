# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:02:22 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""


###1
# def modify1(s):
#     s += "To You"
# msg = "Happy Birthday"
# print("msg:", msg)
# modify1(msg)
# print("msg:", msg)




###2
# x = 'Zokirkhon'
# print(x[2])
# x[2] = "Z" # TypeError: 'str' object does not support item assignment





###3
# name = "Zokirkhon"
# print(name)
# print(id(name))
# name = name + " Kotibkhonov"
# print(name)
# print(id(name))




###4
# def modify1(s):
#     s += "To You"
#     return s
# msg = "Happy Birthday"
# print("msg:", msg)
# value = modify1(msg)
# print(value)







###5
# def modify1(s):
#     s += " To You"
#     print("in callee s=",s,"id=",id(s))
#     return s
# msg = "Happy Birthday"
# print("msg:", msg, id(msg))
# value = modify1(msg)
# print(value)
# print("msg:", msg)







###6
# def modify2(li):
#     li += [100, 200]

# list = [1,2,3,4,5]

# print(list)
# modify2(list)
# print(list)







###7
# def modify2(li):
#     li += [100,200]
#     print(id(li))

# list = [1,2,3,4,5]
# print(id(list))
# print(list)
# modify2(list)
# print(list)







###8
# def area(w,h):
#     result = w*h
#     return result
# print(area(10,20))






###9
# def sub():
#     s= "Bananas are good"
#     print(s)

# sub()







###10
# print(dir())
# print("*"*5)
# x="KKC"
# print(dir())
# print("*"*5)
# print(dir(x))

# def sub():
#     s = "Bananas are good"
#     print("*"*5)
#     print(s)
#     print(dir())
#     print("*"*5)

# sub()
# print(dir())






###11
# def sub():
#     print(s)
# s= "Apples are good" # Global variable then we call faunction
# sub()






###12
# def sub():
#     s= "Bananas are good"
#     print(s)

# s= "Apples are good"
# sub()
# print(s)





###13
# def sub():
#     global s
    
#     print(s)
#     s="Bananas are good"
#     print(s)

# s= "Apples are good"
# sub()
# print(s)








###14
# def sub(x,y):
#     global a # global bo'ldi, tashqarida chaqirilsa ham bunisi birinchi darajali
    
#     a=7
#     x,y=y,x
#     b=3
#     print(a,b,x,y)
# a,b,x,y = 1,2,3,4
# sub(x,y)
# print(a,b,x,y)








###15
# def sub(myList):
#     myList = [1,2,3,4]
#     print(f"myList, is in the function: {myList}")
#     print(id(myList))
#     return

# myList = [10,20,30,40]
# sub(myList)
# print(f"myList, is outside: {myList}")
# print(id(myList))







###16
# def sub(myList):
#     myList += [1,2,3,4] # we write (+=)
#     print(f"myList, is in the function: {myList}")
#     print(id(myList))
#     return

# myList = [10,20,30,40]
# sub(myList)
# print(f"myList, is outside: {myList}")
# print(id(myList))







###17
# PI = 3.14159265358979 # Global variable

# def main():
#     """Return the are of circle and its circumference."""
#     r = float(input("Please enter a radius of circle:\n>>> "))
#     print(f"Area of circle: {circleArea(r)}")
#     print(f"Circumference of circle: {circleCircumference(r)}")

# def circleArea(r):
#     return PI*r*r
# def circleCircumference(r):
#     return 2*PI*r

# main()







###18
# def sub():
#     return 1,2,3
# a,b,c = sub()
# print(a,b,c)







###19
# sum = lambda x,y:x+y;
# print(f"Sum of integers: {sum(10,20)}")
# print(f"Sum of integers: {sum(30,20)}")









###20
# L = [lambda x:x**2, lambda x:x**3, lambda x:x**4]
# print(L[0](2), L[1](2), L[2](2))
# for f in L:
#     print(f(2))
#     print(f(3))
#     print(f(4))
#     print(f(5))
#     print(f(6))






###21
# min = (lambda x,y:x if x<y else y)
# print(min(20,30))



























