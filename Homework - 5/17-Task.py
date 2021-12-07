# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:04:41 2021

@author: Zokirkhon
task: 17. Describe the program below and write the execution result.
"""



with open("phones.txt", "r",encoding="utf-8") as f:
    print(f.readlines())


"""
it will face error because there is not a file with name "phones.txt"
output:

Traceback (most recent call last):
  File "16-task.py", line 10, in <module>
    infile = open("phones.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'phones.txt'
"""










# with open('phones.txt', "w", encoding="utf-8") as f:
#     f.write("홍길동 010-1234-5678")
#     f.write("\n김철수 010-1234-5679")
#     f.write("\n김영희 010-1234-5680")

# after writing above the code , it will be showable.



# with open("phones.txt", "r",encoding="utf-8") as f:
#     print(f.readlines())

# then output will be like this: ['홍길동 010-1234-5678 \n', '김철수 010-1234-5679 \n', '김영희 010-1234-5680']'