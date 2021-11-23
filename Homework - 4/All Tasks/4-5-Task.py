# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:28:47 2021

@author: Zokirkhon
Homework - 4.5
"""


"""
Task: Write the output result of the following program, 
and explain the reason for the output result

직무: 다음 프로그램의 출력 결과가 쓰고, 출력 결과에 대한 이유를 설명하시오
"""


class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age;
obj = Student()
print(obj.__age)
# output: AttributeError: 'Student' object has no attribute '__age'

"""
English:

Because of Encapsulation.
above the program we write self.__age and __name as a private;
we can not get value of that variable straightly.
we can get the value of that variable via methods only.





Korean:

캡슐화 때문입니다.
프로그램 위에 우리는 self.__name을 private으로 씁니다.
우리는 그 변수의 값을 바로 얻을 수 없습니다.
메서드를 통해 해당 변수의 값을 얻을 수 있습니다.

"""