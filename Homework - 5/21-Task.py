# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:06:46 2021

@author: Zokirkhon
task: 21. Describe the following program:
"""

# error handling
try:
    
    # open file
    fh = open("testfile", "r")
    
    # print "fh No error, file opened successfully"
    print("fh Noerror")
    
    # read line 
    str = fh.readline() 

# error handling
except IOError: 
    # error occured with opening file
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다. ") 
    print("error occured with opening file") 
    
# A block that is executed even if an error occurs
finally: 
    print("before file close")
    fh.close()  # testfile이 없을 경우 open하지 못했으므로 close할 수 없음
    print("after file close")
