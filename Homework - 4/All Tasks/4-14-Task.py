# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:44:11 2021

@author: Zokirkhon
Homework - 4.14
"""


"""
Task: Describe the following program

직무: 다음 프로그램을 설명하시오
"""


# define StudentScores as a class
# StudentScores를 클래스로 정의합니다.
class StudentScores(object):
    
    # define the constructor 
    # 생성자를 정의합니다.
    def __init__(self, data):
        self._data = data
        
        # _total calculates the total score with private variable
        # _total은 개인 변수로 총점을 계산합니다.
        self._total = sum(self._data)
    
    # This method checks if two objects are equal.
    # 이 메소드는 두 객체가 같은 것인지 확인하는 메소드입니다.
    def __eq__(self, y):
        return self._total == y._total
    
    # this method checks if the object is greater than the other
    # 이 메서드는 객체가 다른 객체보다 큰지 확인합니다.
    def __lt__(self, y):
        return self._total < y._total
    
    # this method checks if the object is greater than or equal to the other
    # 이 메서드는 개체가 다른 개체보다 크거나 같은지 확인합니다.
    def __le__(self, y):
        return self._total <= y._total


# write the main function
# 메인 함수를 작성합니다.
if __name__ == '__main__':
    # create two objects
    # 두 개의 객체를 생성합니다.
    student_a = StudentScores([90, 95, 100])
    student_b = StudentScores([80, 85, 90])
    
    # check if the objects are equal or greater than the other or not.
    # 객체가 다른 객체보다 크거나 같은지 확인합니다.
    print( student_a == student_b)
    print( student_a < student_b)
