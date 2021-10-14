"""
Created on Tue Oct 12 20:37:05 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""
# Task:
# Describe the following program and write the output.

def get_sum(start, end):
    """ This function returns the sum of numbers from 'start' till the 'end'."""
    sum=0
    for i in range(start, end+1):
        sum+=i
    return sum;
print(get_sum(1,10))

"""
English:

Above the program get_sum() function 
returns the sum of numbers from 'start' till the 'end'.
with for loop.
"""