# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:59:20 2021

@author: Zokirkhon
task: 3. Describe the following program and write the result.
"""
students = [
        ('홍길동', 3.9, 20160303),
        ('김철수', 3.0, 20160302),
        ('최자영', 4.3, 20160301),
]

print(sorted(students, key=lambda x: x[2]))
# sorted by year
# [('최자영', 4.3, 20160301), ('김철수', 3.0, 20160302), ('홍길동', 3.9, 20160303)]


print(sorted(students))
# sorted by student name
# [('김철수', 3.0, 20160302), ('최자영', 4.3, 20160301), ('홍길동', 3.9, 20160303)]

