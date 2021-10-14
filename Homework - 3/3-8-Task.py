"""
Created on Tue Oct 12 21:59:57 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


# Task:
# Explain an anonymous function lambda function


"""
English:

In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, 
anonymous functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.


A lambda function in python has the following syntax.

Syntax of Lambda Function in python


Korean:

Python에서 익명 함수는 이름 없이 정의된 함수입니다.
일반 함수는 Python에서 def 키워드를 사용하여 정의되지만,
익명 함수는 lambda 키워드를 사용하여 정의됩니다.
따라서 익명 함수를 람다 함수라고도 합니다.


파이썬의 람다 함수는 다음과 같은 구문을 가지고 있습니다.

파이썬에서 Lambda 함수의 구문.
"""

# lambda arguments: expression

"""
English:

Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned. 
Lambda functions can be used wherever function objects are required.


Korean:

Lambda 함수는 여러 인수를 가질 수 있지만 하나의 표현식만 가질 수 있습니다.
표현식이 평가되고 리턴됩니다.
Lambda 함수는 함수 객체가 필요한 모든 곳에서 사용할 수 있습니다.
"""



"""
English:

Example of Lambda Function in python
Here is an example of lambda function that doubles the input value.


Korean:

파이썬에서 Lambda 함수의 예
다음은 입력 값을 두 배로 늘리는 람다 함수의 예입니다.
"""

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

# output
# 10;