"""
Created on Fri Oct 15 00:01:35 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Explain Tuple, List, Set and Dictionary












"""
English:

Lists: are just like dynamic sized arrays, declared in other languages 
(vector in C++, ArrayList in Java and Array in JavaScript). 
Lists need not be homogeneous always which makes it a most powerful tool in Python.

Tuple: A Tuple is a collection of Python objects separated by commas. 
In someways a tuple is similar to a list in terms of indexing, 
nested objects and repetition but a tuple is immutable unlike 
lists that are mutable.

Set: A Set is an unordered collection data type that is iterable, 
mutable and has no duplicate elements. Python’s set class represents 
the mathematical notion of a set.

Dictionary: in Python is an unordered collection of data values, 
used to store data values like a map, which unlike other Data Types 
that hold only single value as an element, Dictionary holds key:value pair. 
Key value is provided in the dictionary to make it more optimized.

List, Tuple, Set, and Dictionary are the data structures 
in python that are used to store and organize the data in an efficient manner.


Korean:

목록: 다른 언어로 선언된 동적 크기 배열과 같습니다.
(C++에서는 vector, Java에서는 ArrayList, JavaScript에서는 Array).
목록은 항상 동질일 필요는 없으므로 Python에서 가장 강력한 도구입니다.

튜플: 튜플은 쉼표로 구분된 Python 개체 모음입니다.
어떤 면에서 튜플은 인덱싱 측면에서 목록과 유사합니다.
중첩된 객체와 반복이지만 튜플은
변경 가능한 목록입니다.

세트: 세트는 반복 가능한 정렬되지 않은 컬렉션 데이터 유형입니다.
변경 가능하고 중복 요소가 없습니다. Python의 set 클래스는 다음을 나타냅니다.
집합의 수학적 개념.

사전: Python에서 데이터 값의 정렬되지 않은 컬렉션입니다.
다른 데이터 유형과 달리 맵과 같은 데이터 값을 저장하는 데 사용
단일 값만 요소로 보유하는 Dictionary는 키:값 쌍을 보유합니다.
키 값은 사전에 제공되어 더 최적화됩니다.

List, Tuple, Set 및 Dictionary는 데이터 구조입니다.
효율적인 방식으로 데이터를 저장하고 구성하는 데 사용되는 파이썬에서.
"""


# Python3 program for explaining
# use of list, tuple, set and
# dictionary

#1
# Lists
l = []

# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

#2
# Set
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

#3
# Tuple
t = tuple(l)

# Tuples are immutable
print("Tuple", t)
print()

#4
# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)


# Output
# Adding 5 and 10 in list [5, 10]
# Popped one element from list [5]

# Adding 5 and 10 in set {10, 5}
# Removing 5 from set {10}

# Tuple (5,)

# Dictionary {5: 'Five', 10: 'Ten'}
# Dictionary {5: 'Five'}