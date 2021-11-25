###1
# print(abs(-3))
# print(abs(3+4j))






###2
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(all(lst))
# print(any(lst))
# lst1=[]
# print(all(lst1))
# print(any(lst1))
# lst2=[0]
# print(all(lst2))
# print(any(lst2))







###3
# def any1(iterable):
#     for el in iterable:
#         if el:
#             return True
#     return False

# def all1(iterable):
#     for el in iterable:
#         if not el:
#             return False
#     return True

# list = []
# print(f"any()= {any(list)}")
# print(f"any1()= {any1(list)}")
# print(f"all()= {all(list)}")
# print(f"all1()= {all1(list)}")





###4
# items = ["","a string",0,1,[],{},[1,0],{1,0},[0],[0,],(),(0,)]
# for i in items:
#     print(f"{i}: {bool(i)}")





###5
# print(chr(65))
# print(ord('A'))





###6
# code = compile("a+2","<string>" , "eval")
# a=1
# a = eval(code)
# print(a) #3


# code2 = compile("a2=a2+2","<string>" , "single")
# a2=2
# exec(code2)
# print(a2) #4





###7
# # mode : exec = > 
# s=""
# a=1
# for k in range(10):
#     a+=1
# print(a)

# code = compile(s,'<string>','exec')
# exec(code)









###8
# a = 1
# for k in range(10):
#     a+=1
# print("Compile() function for file")
# print(a)

# # code to run the above file
# s = open("print.py").read() # read the file
# code = compile(s,'<string>','exec')
# exec(code)






###9
# x = complex(4,2)
# print(x)







###10
# class sample:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
# c=sample(1,2)
# print(c.a,c.b)
# delattr(c,'a')
# delattr(c,'b')
# print("******")
# print(c.a,c.b)








###11
# print(dir())
# print("**"*10)
# import os
# print(dir())
# print("**"*10)
# print(dir(os))
# print("**"*10)
# print(dir(abs))
# print("**"*10)








###12
# print(dir([1,2,3]))









###13
# print(divmod(10,7))










###14
# season = ['spring','summer','autumn','winter']
# for i,str in enumerate(season):
#     print(i+1,str)









###15
# x=12
# y=3
# print(eval("x+y"))
# eval("print('Hello world!')")







###16
# exec("name=\"Zokirkhon\"")
# print(name) #Zokirkhon






###17
statements = '''
import math
def area_of_circle(radius):
    return math.pi*radius*radius

'''
# exec(statements)
# print(area_of_circle(5))



# with open('bool.py') as file:
#     lines = file.read()
# print(lines)
# code_object = compile(lines,'bool.py','exec')
# exec(code_object)
# exec(statements)
# print(area_of_circle(5))








###18
# users = [
#     {'gmail':'zokirxonkotibxanov@gmail.com','name':'Zokirkhon','age':23, 'sex':'M'},
#     {'gmail':'gregorythomas@gmail.com','name':'Brett Holland','age':30, 'sex':'M'},
#     {'gmail':'hintonynthia@hotmail.com','name':'Madison Martinez','age':25, 'sex':'F'},
#     {'gmail':'wwagner@gmail.com','name':'Michael Jenkins','age':31, 'sex':'M'},
#     {'gmail':'daniel@gmail.com','name':'Karen Rodriguez','age':35, 'sex':'F'},
#     {'gmail':'ujakson@gmail.com','name':'Amber Rhodes','age':19, 'sex':'F'}
# ]
# def is_man(user):
#     return user['sex'] == "M"

# for man in filter(is_man,users):
#     print(man)









###19
# str = input("Enter a real number: ")
# print(str)
# value = float(str)
# print(value)







###20
# import os
# print(help(os))
# print(help(abs))








###21
# class Student:
#     def __init__(self,name, grade, number):
#         self.name = name
#         self.grade = grade
#         self.number = number
#     def __repr__(self):
#         return repr((self.name,self.grade,self.number))

# students = [
#     Student("Zokirkhon", "3.9", 180421),
#     Student("Sayfullokhon", "3.6", 184895),
#     Student("Bekhzod", "3.0", 123432),
# ]
# print(sorted(students,key=lambda s: s.number))
# print(sorted(students,key=lambda s: s.number, reverse=True))






###22
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __repr__(self):
#         return f"<name: {self.name}, age: {self.age}"

# def keyAge(person):
#     return person.age
# people = [
#     Person("Zokirkhon", 23),
#     Person("Sayfullokhon", 22),
#     Person("Bekhzod", 21),
# ]
# print(sorted(people,key=keyAge))