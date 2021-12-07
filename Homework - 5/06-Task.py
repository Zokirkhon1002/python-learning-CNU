# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:42:20 2021

@author: Zokirkhon
task: 6. Describe the following program and write the result.
"""



from copy import deepcopy
x = [1,2,3]
lst = [1,2,x]
lst1 = deepcopy(lst)

print(id(lst))
# output: 1872973925960

print(id(lst1))
# output: 1872973926216

print(id(lst1) == id(lst))
# output: False


"""
English:

Deep copy is a process in which the copying process occurs recursively. 
It means first constructing a new collection object and then recursively 
populating it with copies of the child objects found in the original. 
In case of deep copy, a copy of object is copied in other object. 
It means that any changes made to a copy of object do not reflect in the original object. 
In python, this is implemented using “deepcopy()” function.


Korean: 

딥 카피는 복사 프로세스가 재귀적으로 발생하는 프로세스입니다.
먼저 새로운 컬렉션 객체를 생성한 다음 재귀적으로 생성하는 것을 의미합니다.
원본에서 찾은 자식 개체의 복사본으로 채웁니다.
Deep Copy의 경우 객체의 복사본이 다른 객체에 복사됩니다.
이는 개체 복사본에 대한 변경 사항이 원본 개체에 반영되지 않음을 의미합니다.
파이썬에서는 "deepcopy()" 함수를 사용하여 구현합니다.

"""

