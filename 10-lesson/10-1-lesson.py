
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:57:11 2021

@author: Zokirkhon Kotibkhonov
topic: Special Methods
"""




###1
# class Vector2D():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "({},{})".format(self.x,self.y)
#     def add(self,other):
#         return Vector2D(self.x + other.x, self.y + other.y)

# v1 = Vector2D(30,40)
# v2 = Vector2D(10,20)
# v3 = v1.add(v2) # Vector2D's add method is called
# print(f"v1.add(v2)={v3}")







###2
# class Vector2D():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
    
#     def __add__(self,other):
#         return Vector2D(self.x+other.x, self.y+other.y)
#     def __sub__(self,other):
#         return Vector2D(self.x-other.x, self.y-other.y)
    
    
#     def __str__(self):
#         return "({},{})".format(self.x,self.y)

# v1 = Vector2D(30,40)
# v2 = Vector2D(10,20)
# v3 = v1 + v2 # Vector2D's special method which is __add__ method is called
# print(f"v1+v2={v3}")
# v4 = v1- v2;
# print(f"v1-v2={v4}")







###3
# class Car(object):
#     def __init__(self,name):
#         self.name = name
    
#     def __str__(self):
#         return f"Type: Car, Name: {self.name}"
    
#     def __repr__(self):
#         return f"Car('{self.name}')"

# if __name__ == '__main__':
#     my_car = Car("Hyundai")
#     my_car_string = str(my_car)
    
#     print(my_car_string)
#     print(my_car)
    
#     my_car_repr = repr(my_car)
#     print(my_car_repr)
    
#     my_car1 = eval(my_car_repr)
#     print(my_car is my_car1)






###4
### The eval() function is a built-in function that 
### executes a Python expression and gets the result.
# x = 1;
# print(eval("x+1")) # returns 2








###5
### Square_iterator class
# class Square(object):
#     def __init__(self,start,end):
#         self._number = start-1
#         self._end = end
    
#     def __iter__(self):
#         return self;
    
#     def __next__(self):
#         if self._number == self._end:
#             raise StopIteration
#         else:
#             self._number = self._number + 1
#             return self._number**2;

# if __name__ == "__main__":
#     squares = iter(Square(1,5))
#         # Get the iterator of Square object
#         # The iter method is automatically called when we use the for loop
#     for item in squares: #The iterator is used in the for statement and value is retrieved.
#         print(item, end=" ")
    
#     print()
    
#     squares = iter(Square(1,3))
#     print(next(squares)) # call next method to get the next value
#     print(next(squares))
#     print(next(squares))
#     print(next(squares)) # if the last range is exceeded, StopIteration error occurs.

### 1 4 9 16 25
### 1
### 4
### 9
### Traceback (most recent call last):
###   File "D:\Coding Class\Self study from Videos\Python programming\Chonnam National University\10-lesson\spMethod.py", line 134, in <module>
###     print(next(squares)) # if the last range is exceeded, StopIteration error occurs.
###   File "D:\Coding Class\Self study from Videos\Python programming\Chonnam National University\10-lesson\spMethod.py", line 116, in __next__
###     raise StopIteration
### StopIteration






###6
# class test():
#     def __call__(self):
#         print("callable")

# obj=test()
# print(obj)
# print(obj().__call__())






###7
# import random
# class Dice(object):
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
    
#     def __call__(self):
#         return random.randint(self.start,self.end)

# if __name__ == '__main__':
#     dice = Dice(1,6)
#     print(dice()) # returns a random number between 1 and 6






###8
# class StudentScores(object):
#     def __init__(self,data):
#         self.data = data
    
#     def __len__(self):
#         return len(self.data)
    
#     def __contains__(self,item):
#         return item in self.data

# if __name__ == '__main__':
#     student_scores = StudentScores([90,80,70,60,50,100])
#     print(len(student_scores))
#     print(60 in student_scores)
#     print(40 in student_scores)

# # output:
# # 6
# # True
# # False






###9
# class StudentDic(object):
#     def __init__(self):
#         self._data = {}
    
#     def __getitem__(self,key):
#         return self._data[key]
    
#     def __setitem__(self,key,value):
#         self._data[key] = value
    
#     def __delitem__(self,key):
#         if key in self._data:
#             del self._data[key]
#             print("{} is deleted".format(key))
#         else:
#             print("{} is not in the dictionary".format(key))

# if __name__ == '__main__':
#     student_a = StudentDic()
#     student_a['name'] = "Zokirkhon"
#     print(student_a['name'])
#     del student_a['name'];
#     print(student_a['name'])








###10
# class StudentScores(object):
#     def __init__(self,data):
#         self._data = data
#         self._total = sum(self._data)
    
#     def __eq__(self,y):
#         return self._total == y._total
    
#     def __lt__(self,y):
#         return self._total == y._total
    
#     def __le__(self,y):
#         return self._total == y._total

# if __name__ == '__main__':
#     student_a = StudentScores([90,80,70,100])
#     student_b = StudentScores([60,65,70,99])
#     print(student_a == student_b)
#     print(student_a < student_b)






###11
# class Circle:
#     PI = 3.14
#     def __init__(self,name,radius):
#         self.name = name
#         self.radius = radius

# c1 = Circle("C1",4)
# print(f"Attribute of C1: ${c1.__dict__}")
# # Value can be obtained in [key] format.
# print(f"Name of C1: {c1.__dict__['name']}")
# print(f"Radius of C1: {c1.__dict__['radius']}")





###12
class docAttr():
    """
    explain Docstring
    __doc__ is a built-in attribute of class.
    """
    def __init__(self,name):
        self.name = name
        print("Construct")

doc = docAttr("Zokirkhon")
print(doc.__doc__)