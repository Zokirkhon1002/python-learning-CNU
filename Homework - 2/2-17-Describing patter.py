# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:49:49 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Describing the following program and write the output.




for y in range(5):
    # The outer loop to print the number of rows.
    # 행 수를 인쇄하는 외부 루프.
    for x in range(10):
        # The inner loops to print the number of columns.
        # 열 수를 인쇄하는 내부 루프.
        print("*",end="")
    
    # ending line after each row  
    # 각 행 뒤의 끝줄 .
    print("")

# output
# **********
# **********
# **********
# **********
# **********


# Another way:

result = ("*"*10 + "\n")*5
print(result)

# output
# **********
# **********
# **********
# **********
# **********

