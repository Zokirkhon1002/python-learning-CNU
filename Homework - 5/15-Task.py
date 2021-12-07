# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:44:58 2021

@author: Zokirkhon
task: 15. Describe the program below and write the execution result.
"""



outfile = open("phones.txt", "w") # open file for writing but it fails, cause we have to write with "with open() as something"
outfile.write("홍길동 010-1234-5678")
outfile.write("김철수 010-1234-5679")
outfile.write("김영희 010-1234-5680")
outfile.close() 

# 파일을 열고 파일에 저장한다.
"""
output: 
Traceback (most recent call last):
  File "15-task.py", line 25, in <module>
    outfile.write("홍길동 010-1234-5678")
  File "C:\Program Files\Python37\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-2: character maps to <undefined>
"""