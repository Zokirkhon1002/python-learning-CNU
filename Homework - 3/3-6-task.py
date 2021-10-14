"""
Created on Tue Oct 12 21:11:58 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


# Task:
# Describe local and global variables and the keyword global



"""
English:

In Python, there are two main types of variables: local and global.
Global variables are variables declared outside of a function. 
Global variables have a global scope. This means that they can be 
accessed throughout an entire program, including within functions.

A global variable can be accessed throughout a program.

Here is an example of a global variable in Python:


Korean:

Python에는 두 가지 주요 유형의 변수가 있습니다: 로컬 및 전역.
전역 변수는 함수 외부에서 선언된 변수입니다.
전역 변수에는 전역 범위가 있습니다. 이것은 그들이 될 수 있음을 의미합니다
함수 내를 포함하여 전체 프로그램에서 액세스합니다.

전역 변수는 프로그램 전체에서 액세스할 수 있습니다.

다음은 Python의 전역 변수 예입니다.

"""
name = "Zokirkhon Kotibkhonov"



""" 
English:

Once we declare a global variable, we can use it throughout our code. 
For example, we can create a function that prints the value held by 
our global variable name using the following code:


Korean:

전역 변수를 선언하면 코드 전체에서 사용할 수 있습니다.
예를 들어, 다음이 보유한 값을 인쇄하는 함수를 만들 수 있습니다.
다음 코드를 사용하여 전역 변수 이름:

"""
def printName():
	print(name)

printName()




"""
English:

Python Local Variables
Local variables, on the other hand, are variables declared inside a function. 
These variables are known to have local scope. This means they can be accessed 
only within the function in which they are declared.

A local variable can only be accessed within a particular function.
The following is an example of a program that uses a local variable:


Korean:

파이썬 지역 변수
반면에 지역 변수는 함수 내부에 선언된 변수입니다. 
이러한 변수는 로컬 범위가 있는 것으로 알려져 있습니다. 
즉, 선언된 함수 내에서만 액세스할 수 있습니다.

지역 변수는 특정 함수 내에서만 액세스할 수 있습니다.
다음은 지역 변수를 사용하는 프로그램의 예입니다.

"""

def printName2():
	name = "Abdulloh"
	print(name)

printName2()

