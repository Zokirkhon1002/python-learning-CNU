"""
Created on Fri Oct 15 02:36:40 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

#Task:
# Write the result of the program below in ().

x = ["ab","xdf","cd","Acd","Trs","z","abcde"]
x.sort(key=str.lower)
print(x)
# Output
# ['ab', 'abcde', 'Acd', 'cd', 'Trs', 'xdf', 'z']

x = ["ab","xdf","cd","Acd","Trs","z","abcde"]
x.sort()
print(x)
# Output
# ['Acd', 'Trs', 'ab', 'abcde', 'cd', 'xdf', 'z']

x.sort(key=len)
print(x)
# Output
# ['z', 'ab', 'cd', 'Acd', 'Trs', 'xdf', 'abcde']
