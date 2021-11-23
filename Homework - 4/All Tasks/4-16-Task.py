# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:18:58 2021

@author: Zokirkhon
Homework - 4.16
"""


"""
Task: Describe the following program and write the output..

직무: 다음 프로그램을 설명하고, 출력 결과를 쓰시오
"""

# importing datetime module
# datetime 모듈을 불러옵니다.
import datetime

# defining a function with a parameter which type is function
# 함수를 정의하고 함수의 인자로 함수를 정의합니다.
def deco2(func):
    
    # defining a inner function
    # 내부 함수를 정의합니다.
    def new_func():
        
        # printing Today as a string and today's date
        # 오늘을 문자열로 출력하고 오늘의 날짜를 출력합니다.
        print("Today", datetime.date.today())
        
        # calling the function which is passed as a parameter
        # 매개변수로 전달되는 함수를 호출합니다.
        func()
    
    # returning the inner function
    # 내부 함수를 반환합니다.
    return new_func

# calling the function deco2
# deco2 함수를 호출합니다.
@deco2
# writing the function which is passed as a parameter
# 매개변수로 전달되는 함수를 작성합니다.
def print_hi4():
    # printing the string
    # 문자열을 출력합니다.
    print("Hello Python")
# calling the function which is passed as a parameter
# 매개변수로 전달되는 함수를 호출합니다.
print_hi4()

# calling the function deco2
# deco2 함수를 호출합니다.
@deco2
# writing the function which is passed as a parameter
# 매개변수로 전달되는 함수를 작성합니다.
def print_easy():
    # printing the string
    # 문자열을 출력합니다.
    print("Python is easy.")
# calling the function which is passed as a parameter
# 매개변수로 전달되는 함수를 호출합니다.
print_easy()



# output:
# Today 2021-11-23
# Hello Python
# Today 2021-11-23
# Python is easy.