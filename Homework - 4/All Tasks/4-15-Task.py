# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:09:41 2021

@author: Zokirkhon
Homework - 4.15
"""


"""
Task: Describe the following function, and write the result.

직무: 다음 프로그램을 설명하고 출력 결과를 쓰시오.
"""


# define the function
# 함수를 정의합니다.
def outter():
    # define a variable
    # 변수를 정의합니다.
    a=1	
    # define an inner function	
    # 내부 함수를 정의합니다.		
    def inner1():
        # define a variable
        # 변수를 정의합니다.
        b=2		
        
        # define an inner function
        # 내부 함수를 정의합니다.
        def inner2():
            
            # define a variable
            # 변수를 정의합니다.
            c=3
            
            # print the result of the inner function which is inner2
            # inner2인 내부 함수의 결과를 출력합니다.
            print("inner2")
            
            # print the result of the inner function which are a, b, c
            # a, b, c인 내부 함수의 결과를 출력합니다.
            print(a,b,c)
            
        # print the result of the inner function which is inner1
        # inner1인 내부 함수의 결과를 출력합니다.
        print("inner1")
        
        # calling the inner function which is inner2
        # inner2인 내부 함수를 호출합니다.
        inner2()
    
    # print the outer function which is in the outter function
    # outter인 외부 함수의 결과를 출력합니다.
    print("outter")
    
    # calling the inner function which is inner1
    # inner1인 내부 함수를 호출합니다.
    inner1()

# calling the outter function
# outter인 외부 함수를 호출합니다.
outter()


# output:

# outter
# inner1
# inner2
# 1 2 3

