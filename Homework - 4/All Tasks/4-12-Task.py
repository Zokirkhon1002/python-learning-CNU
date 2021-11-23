# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:18:41 2021

@author: Zokirkhon
Homework - 4.12
"""


"""
Task: Describe the following function, and write the result in ( ).

직무: 다음 함수를 설명하고, (	) 안에 결과를 쓰시오
"""


print(chr(65))
# Output:
# A
print(ord('A'))

# Output:
# 65

"""
English:

When it comes to describe above the function.
"ord()" function that transfer the character or string to ASCII 
and 
"chr()" function that transfer the number from ASCII to string or character




Korean:

위의 기능을 설명하자면. 문자 또는 문자열을 ASCII로 
전송하는 "ord()" 함수와 ASCII에서 숫자를 문자열 또는 
문자로 전송하는 "char()" 함수.

"""




# following code is ascii table
# 다음 코드는 ASCII 테이블입니다.

for i in list(range(128)):
    print(chr(i))

