# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 06:01:02 2021

@author: Zokirkhon
topic: Functions
"""



###1
# def func_name():
#     print("Hello World")
#     print("Call function")
#     print("End function")

# func_name()







###2
# def sum_num(x,y):
#     print(x+y)

# a=20
# sum_num(a,30);







###3
# def sum_add_num(x,y):
#     x+=3
#     print(x,y)

# outer = 77
# sum_add_num(outer,100);







###4
# def progression(n,step=1):
#     x=1;
#     while x<=n:
#         print(x)
#         x += step;

# progression(10)
# progression(11,2)







###5
# def datefunc(year,month,day):
#     print(f"year: {year} month: {month} day: {day}")
# datefunc(2020,11,14)
# datefunc(2021,11,14)
# datefunc(2018,11,15)






###6
# def argsfunc(*args):
#     i=0
#     for x in args:
#         i+=1;
#     print(f"{i} arguments")
#     print(args)

# argsfunc(1,2,(3,4,5))
# # output:
# # 3 arguments
# # (1, 2, (3, 4, 5))

# argsfunc(1,[7,55],"Test",{'a':1,'b':100})
# # output:
# # 4 arguments
# # (1, [7, 55], 'Test', {'a': 1, 'b': 100})

# a,b,c = 1,(3,6,9),{'x':0,'y':99}
# argsfunc(a,b,c)
# # output:
# # 3 arguments
# # (1, (3, 6, 9), {'x': 0, 'y': 99})







###7
# def dictsfunc(**kwargs):
#     i=0
#     for x in kwargs:
#         i+=1;
#     print(f"{i} arguments")
#     print(kwargs)

# dictsfunc(a=1,b=2,c=3)
# # output:
# # 3 arguments
# # {'a': 1, 'b': 2, 'c': 3}

# dictsfunc(a=1,b=2,c=3,d=4,e=5)
# # output:
# # 5 arguments
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}






###8
# def recommandable(a,*args):
#     print(a,args)

# recommandable(1,2,3,4,5)







###9
# def recommandable(a,*args,**kwargs):
#     print(a,args,kwargs)

# recommandable(1,2,3,4,5,ab='ab',ac='xx')
# recommandable(1,2,3,4,5,{'a':6,'b':7})
# recommandable(1,2,3,4,5,ab='ab',ac='xx')
# # recommandable(1,2,3,4,5,'b'=7) # error
# # recommandable(1,2,3,4,5,ab:'ab',ac:'xx') # error









###10
# def returnTest(a,b,c,d):
#     print(a+b)
#     return b+c
#     print(c+d) # there is no return statement

# returnTest(1,2,3,4)








###11
# def returnTest(a,b,c,d):
#     print(a+b)
#     return b+c
#     print(c+d) # there is no return statement

# returnTest(1,2,3,4) # output: 3
# print("return test")    # output: return test
# ret=returnTest(1,2,3,4) # output: 3 
# print(ret); # output: 5






###12
def reTuple(x,y,z):
    return x,y,z
print(reTuple(1,2,3))   # output: (1, 2, 3)

a,b,c = reTuple(8,9,10)
print(a,b,c)    # output: 8 9 10