"""
Created on Mon Oct 12 22:10:23 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


# Task:
# Describe the following program.

L = [lambda x:x**2,lambda x:x**3,lambda x:x**4]
for f in L:
    print(f(3))

# Output
# 9
# 27
# 81


"""
English:

In the example above, a list of three functions was built up by embedding 
lambda expressions inside a list. 
A def won't work inside a list literal like this because it is a statement, not an expression.
first function returns square of x, second returns cube of x, and third returns 4 power of x.
with for loop printed with each function square of 3, cube of 3, and 4 power of 3.


Korean:

위의 예에서 다음을 포함하여 세 가지 함수 목록을 작성했습니다.
목록 내부의 람다 표현식.
def는 표현식이 아니라 명령문이기 때문에 이와 같은 목록 리터럴 내에서 작동하지 않습니다.
첫 번째 함수는 x의 제곱을 반환하고, 두 번째 함수는 x의 세제곱을 반환하고, 세 번째 함수는 x의 4제곱을 반환합니다.
for 루프는 3의 제곱, 3의 세제곱, 3의 4제곱으로 각 함수를 인쇄합니다.
"""

