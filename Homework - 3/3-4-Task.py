"""
Created on Mon Oct 12 20:48:27 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Tak:
# Describe two ways to pass arguments in a function.

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


