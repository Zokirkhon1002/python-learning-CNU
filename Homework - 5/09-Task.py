# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:10:37 2021

@author: Zokirkhon
task: . Describe the following program
"""

import sys
# sys module is used to get the input from the user in cmd or terminal

if __name__=="__main__":
    # if the program is run directly, then run the following code
    
	print("Number of argv:", len(sys.argv)) 
    # len() is used to get the length of the argv
    
	for item in sys.argv:
        # for loop is used to iterate through the argv
        
		print(item) 
        # print the argv



# output: 
# Number of argv: 3
# 09-Task.py
# Hello
# World