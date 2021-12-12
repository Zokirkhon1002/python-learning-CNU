# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:32:15 2021

@author: Zokirkhon
@topic: handling files and exceptions
"""

###1
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     except:
#         print("something went wrong")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# divide(None, 0)








###2
# try:
#     raise TypeError("There was a type error")
# except TypeError as err:
#     print(err.args)









class AgeException(Exception):
    # class named AgeException

    def __init__(self, msg):
        # constructor with one parameter which is a message the type is string

        self._message = msg


def input_age():
    # function named input_age

    age = int(input("나이를 입력해 주세요: ")) 
    # input age from user and convert to integer

    if age < 0: 
    # if age is less than 0

        raise AgeException("나이는 음수가 될 수 없습니다.") 
        # raise exception with message "age cannot be negative"
    
    elif age > 150: 
    # if age is greater than 150
        raise AgeException("150세 이상 살 수 있을 까요?") 
        # raise exception with message "Can you live over 150?"
    else: 
    # if age is between 0 and 150
        return age 
        # return age


if __name__ == "__main__": 
# if this file is run directly

    try: 
    # try to run the following code
        age = input_age() 
        # input age from user 
    except AgeException as e: # if exception occurs 
        print(e.args[0]) 
        # print exception message
    else: 
    # if no exception occurs
        print("나이는 %d세입니다." % age)
        # print age 
