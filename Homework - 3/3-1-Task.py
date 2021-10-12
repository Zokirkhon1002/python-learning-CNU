"""
Created on Mon Oct 12 19:45:34 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""
# Task:
# Describe the function and explain why the function is needed


####1 Why functions are needed?
#### Answer
"""
English:

Functions are an essential part of most programming languages. 
Functions are reusable pieces of code that can be called 
using a function's name. Functions can be called anywhere in a Python program, 
including calling functions within other functions.

Functions provide a couple of benefits:
    Functions allow the same piece of code to run multiple times
    Functions break long programs up into smaller components
    Functions can be shared and used by other programmers


Korean:

함수는 대부분의 프로그래밍 언어에서 필수적인 부분입니다.
함수는 호출할 수 있는 재사용 가능한 코드 조각입니다.
함수의 이름을 사용합니다. 함수는 파이썬 프로그램의 어디에서나 호출할 수 있습니다.
다른 함수 내에서 함수 호출 포함.

함수는 다음과 같은 몇 가지 이점을 제공합니다.
     함수를 사용하면 동일한 코드를 여러 번 실행할 수 있습니다.
     함수는 긴 프로그램을 더 작은 구성 요소로 나눕니다.
     기능은 다른 프로그래머가 공유하고 사용할 수 있습니다.
"""



####2 Describe Functions
#### Answers

"""
English:

A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.


Korean:

함수는 호출될 때만 실행되는 코드 블록입니다.
매개변수라고 하는 데이터를 함수에 전달할 수 있습니다.
함수는 결과로 데이터를 반환할 수 있습니다.
"""


"""
English:

Creating a Function
In Python a function is defined using the "def" keyword:


Korean:

함수 생성
Python에서 함수는 "def" 키워드를 사용하여 정의됩니다.
"""


def my_function():
    print("Hello World!, from function")


"""
English:

Calling a Function
To call a function, use the function name followed by parenthesis:


Korean:

함수 호출
함수를 호출하려면 함수 이름 다음에 괄호를 사용하십시오.
"""

my_function()


"""
English:

Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (name).
When the function is called, we pass along a first name, which is used inside the function to print the full name:


Korean:

인수
정보는 인수로 함수에 전달할 수 있습니다.
인수는 함수 이름 뒤에 괄호 안에 지정됩니다.
원하는 만큼 인수를 추가할 수 있으며 쉼표로 구분하면 됩니다.
다음 예제에는 하나의 인수(fname)가 있는 함수가 있습니다.
함수가 호출되면 이름을 전달합니다. 이름은 전체 이름을 인쇄하기 위해 함수 내부에서 사용됩니다.
"""


def my_function2(name):
    """ This function returns saying Hello for argument name."""
    print(f"Hello, {name}")


my_function2("Zokirkhon")


"""
English:

Parameters or Arguments
The terms parameter and argument can be used for the same thing:
information that are passed into a function.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.


Korean:

매개변수 또는 인수
매개변수와 인수라는 용어는 같은 용도로 사용할 수 있습니다.
함수에 전달되는 정보.

함수의 관점에서:
매개변수는 함수 정의에서 괄호 안에 나열된 변수입니다.
인수는 호출될 때 함수에 전송되는 값입니다.
"""


"""
Number of Arguments.
By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments, you have to call the function
with 2 arguments, not more, and not less.


Korean:

인수의 수.
기본적으로 함수는 올바른 수의 인수로 호출되어야 합니다.
함수가 2개의 인수를 예상하는 경우 함수를 호출해야 함을 의미합니다.
더도 말고 덜도 말고 2개의 인수로.
"""


def my_function3(first_name, second_name):
    print(f"Hello, {first_name}, {second_name}.")


my_function3("Zokirkhon", "Kotibkhonov")
# If you try to call the function with 1 or 3 arguments, you will get an error:
# 1개 또는 3개의 인수로 함수를 호출하려고 하면 오류가 발생합니다.


"""
English:

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:


Korean:

임의 인수, *args
함수에 전달할 인수의 수를 모르는 경우
함수 정의에서 매개변수 이름 앞에 *를 추가하십시오.
이런 식으로 함수는 튜플 인수를 수신하고 그에 따라 항목에 액세스할 수 있습니다.
"""


def my_function4(*firneds):
    print("My friends are: ", end=" ")
    for i in firneds:
        print(i, end=", ")


my_function4("Ali", "Abdullo", "Olim")


"""
English:

Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.


Korean:

키워드 인수
key = value 구문을 사용하여 인수를 보낼 수도 있습니다.
이런 식으로 인수의 순서는 중요하지 않습니다.
"""


def my_function5(first, second, third):
    print(f"My friends are: {first}, {second}, {third}")


my_function5(third="Ali", first="Abdullo", second="Olim")


"""
English:

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:


Korean:

임의의 키워드 인수, **kwargs
함수에 전달할 키워드 인수의 수를 모르는 경우
두 개의 별표를 추가하십시오. ** 함수 정의의 매개변수 이름 앞에.
이런 식으로 함수는 인수 사전을 수신하고 그에 따라 항목에 액세스할 수 있습니다.
"""


def my_function6(**names):
    print(f"His last name is {names['lname']}")


my_function6(fname="Zokirkhon", lname="Kotibkhonov")


"""
English:

Default Parameter Value
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:


Korean:

기본 매개변수 값
다음 예는 기본 매개변수 값을 사용하는 방법을 보여줍니다.
인수 없이 함수를 호출하면 기본값을 사용합니다.
"""


def my_function7(country="Uzbekistan"):
    print(f"I am living  in {country}")


my_function7("South Korea")
my_function7()


"""
English:

Return Values
To let a function return a value, use the return statement:


Korean:

반환 값
함수가 값을 반환하도록 하려면 return 문을 사용합니다.
"""


def my_function8(x, y):
    """ This function returns the y power of x"""
    return x**y

print(my_function8(3,3))
