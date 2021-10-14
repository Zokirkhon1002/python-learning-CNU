"""
Created on Fri Oct 15 03:23:22 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

#Task:
# Write the result of the program below in ().


aa = [
    [1,2,3,4],
    [5,6],
    [7,8,9]
    ]

print(aa[1][0])
# Output
# 5

print(aa[2][1])
# Output
# 8


# if we want to print all numbers in array. we write a program like this:

rows = len(aa)
for r in range(rows):
    cols = len(aa[r])
    for c in range(cols):
        print(aa[r][c], end=',')
    print()

# Output
# 1,2,3,4,
# 5,6,
# 7,8,9,