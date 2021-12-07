# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:10:00 2021

@author: Zokirkhon
task: 20. Describe the exception and how to handle the exception
"""


"""
English:

Error in Python can be of two types i.e. Syntax errors and Exceptions. 
Errors are the problems in a program due to which the program will stop the execution. 
On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 

Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program. 

Example:



Korean:

Python의 오류는 구문 오류와 예외의 두 가지 유형이 있습니다.
오류는 프로그램이 실행을 중지하는 프로그램의 문제입니다.
반면에 프로그램의 정상적인 흐름을 변경하는 일부 내부 이벤트가 발생하면 예외가 발생합니다.

구문 오류와 예외의 차이점
구문 오류: 이름에서 알 수 있듯이 이 오류는 코드의 잘못된 구문으로 인해 발생합니다. 프로그램 종료로 이어집니다.

예시:
"""
# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

"""
output:
File "20-task.py", line 40    
if(amount > 2999)                    
^SyntaxError: invalid syntax
"""




"""
English:

Exceptions: Exceptions are raised when the program is syntactically correct, 
but the code resulted in an error. This error does not stop the execution of the program, 
however, it changes the normal flow of the program.

Example:


Korean:

예외: 프로그램이 구문적으로 올바르면 예외가 발생합니다.
그러나 코드에서 오류가 발생했습니다. 이 오류는 프로그램 실행을 중지하지 않으며,
그러나 프로그램의 정상적인 흐름을 변경합니다.

예시:
"""
# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)

""" output: 
Traceback (most recent call last):  
File "20-task.py", line 75, in <module>    
a = marks / 0
ZeroDivisionError: division by zero
"""




"""
English:

Try and Except Statement – Catching Exceptions
Try and except statements are used to catch and handle exceptions in Python. 
Statements that can raise exceptions are kept inside the try clause and 
the statements that handle the exception are written inside except clause.

Example: Let us try to access the array element whose index is out of bound 
and handle the corresponding exception.


Korean:

Try and except 문 – 예외 잡기
Try 및 except 문은 Python에서 예외를 catch하고 처리하는 데 사용됩니다.
예외를 일으킬 수 있는 문은 try 절 안에 보관되며
예외를 처리하는 명령문은 except 절 안에 작성됩니다.

예: 인덱스가 범위를 벗어난 배열 요소에 액세스하려고 합니다.
해당 예외를 처리합니다.
"""

# Python program to handle simple runtime error

a = [1, 2, 3]
try:
	print (f"Second element = {a[1]}")
	# Throws error since there are only 3 elements in array
	print (f"Fourth element = {a[3]}")
except:
	print ("There is only 3 elements in array")





# Catching Specific Exception
# 특정 예외 잡기

# Program to handle multiple errors with one
# except statement

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)


try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions

except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
	print("ZeroDivisionError가 발생하여 처리되었습니다.")
except NameError:
	print("NameError Occurred and Handled")
	print("NameError 발생 및 처리 되었습니다.")





# Try with Else Clause
# Else 절로 시도.

# Program to depict else clause with try-except
# Function which returns a/b

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
