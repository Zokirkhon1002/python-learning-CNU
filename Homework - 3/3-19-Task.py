"""
Created on Fri Oct 15 01:58:33 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Describe the following program and write the output.

# dictionary comprehensions can be used to create dictionaries from arbitrary key and value expressions:
# 사전 이해를 사용하여 임의의 키 및 값 표현식에서 사전을 만들 수 있습니다.
dict1={x:x*x*x for x in range(5)}
    # in here: from 0 till 5 , returning the cube of each number as a dictionary
    # 여기에서: 0에서 5까지, 각 숫자의 큐브를 사전으로 반환합니다.
print(dict1)
# And we printed dictionary
# 그리고 사전을 인쇄했습니다.


# output 
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}