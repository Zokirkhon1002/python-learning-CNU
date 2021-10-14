"""
Created on Fri Oct 15 02:46:47 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

#Task:
# Write the result of the program.

def func2(list):
    print(f"list = {list}, id = {id(list)}, Inside of Function")
    # Output 
    # list = [0, 1, 2, 3, 4, 5], id = 2166806377664, Inside of Function
    list[2]=100
    print(f"list = {list}, id = {id(list)}, Inside of Function")
    # Output 
    # list = [0, 1, 100, 3, 4, 5], id = 2166806377664, Inside of Function
values=[0,1,2,3,4,5]
print(f"values = {values}, Outside of Function")
# Output 
# values = [0, 1, 2, 3, 4, 5], Outside of Function

func2(values)

print(f"values = {values}  Outside of Function")
# Output
# values = [0, 1, 100, 3, 4, 5]  Outside of Function

