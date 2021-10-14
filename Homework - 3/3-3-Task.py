"""
Created on Tue Oct 12 20:44:55 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Tak:
# Explain default arguments and keyword arguments in functions.



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
