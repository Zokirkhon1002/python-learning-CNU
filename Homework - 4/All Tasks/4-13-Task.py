# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:32:11 2021

@author: Zokirkhon
Homework - 4.13
"""


"""
Task: Write the result of the following program

직무: 다음 프로그램의 결과를 쓰시오
"""


students = [
        ('홍길동', 3.9, 303),
        ('김철수', 3.0, 302),
        ('최자영', 4.3, 301)
]
print(sorted(students, key=lambda x: x[2]))
# Output:
# [('최자영', 4.3, 301), ('김철수', 3.0, 302), ('홍길동', 3.9, 303)]
print(sorted(students))
# Output:
# [('김철수', 3.0, 302), ('최자영', 4.3, 301), ('홍길동', 3.9, 303)]


