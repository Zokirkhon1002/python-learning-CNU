# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:52:02 2021

@author: Zokirkhon
task: 7. Explain the following code.
"""
import random
a,b,start,stop,step = 2,4,1,50,2;


random.randrange(start, stop, step)
# random.randrange() returns a random integer N such that start <= N < stop. 
# step is the increment (or decrement) between successive values.
# The default value of step is 1.

# random.randrange()는 start <= N < stop이 되는 임의의 정수 N을 반환합니다.
# 단계는 연속 값 사이의 증가(또는 감소)입니다.
# 단계의 기본값은 1입니다.

random.randint(a, b)
# random.randint() return a number between a and b, including both endpoints.
# random.randint()는 두 끝점을 포함하여 b와 b 사이의 숫자를 반환합니다.

random.random()
# random.random() returns a random float x such that 0.0 <= x < 1.0.
# random.random()은 0.0 <= x < 1.0이 되는 임의의 float x를 반환합니다.

