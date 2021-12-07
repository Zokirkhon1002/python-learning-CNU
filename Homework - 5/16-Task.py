# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:58:18 2021

@author: Zokirkhon
task: 16. Describe the program below and write the execution result.
"""


infile = open("phones.txt", "r")
line = infile.readline()
while line != "":
	print(line);
	line = infile.readline()
infile.close() 
# The program reads the file and prints the lines. but it faces error cause there is no file such as "phones.txt"

"""
Traceback (most recent call last):
  File "16-task.py", line 10, in <module>
    infile = open("phones.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'phones.txt'
"""


