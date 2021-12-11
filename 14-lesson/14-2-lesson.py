# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:08:01 2021

@author: Zokirkhon
topic: handling files and exceptions
"""



###1
# output_file = open("output.txt", "w")

# for i in range(10):
#     output_file.write("\nAppend this to the file")

# output_file.close()






###2
# infile = open("proverb.txt", "r")
# for line in infile:
#     print(line)
# infile.close()







###3
# infile = open("proverb.txt", "r")
# for line in infile:
#     print(line.rstrip())
# infile.close()






###4
# infile = open("proverb.txt", "r")
# for line in infile:
#     line = line.rstrip()
#     word_list = line.split()
#     for word in word_list:
#         print(word)
# infile.close()







###5
# infile = open("proverb.txt", "r")
# for line in infile:
#     line = line.rstrip()
#     word_list = line.split('a') # split the line at the 'a' letter
#     print(word_list)
# infile.close()








###6
# infile = open("numbers.txt", "w")
# for i in range(10):
#     infile.write(f"{i} ")
# infile.close()









###7
# from os import read
# from tkinter import *
# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfilename

# read_file = askopenfilename()
# if(read_file != None):
#     infile = open(read_file, "r")
#     for lin in infile.readlines():
#         print(lin.strip())
#     infile.close()
# else:
#     print("No file selected")
#     exit()




# ###8
# def parse_file(path,rw='r'):
#     infile = open(path, rw)
#     spaces=0
#     tabs=0
#     for line in infile:
#         spaces += line.count(" ")
#         tabs += line.count("\t")
#     infile.close()
    
#     return spaces, tabs;

# filename = input("Enter the file name: ")
# spaces,tabs = parse_file(filename)
# print(f"Spaces: {spaces}\n Tabs: {tabs}")






###9
# filename = input("Enter the file name: ")
# infile = open(filename, "r")
# outfile = open('result.txt','w')

# for index, line in enumerate(infile):
#     outfile.write(f"{index+1}: {line}")
#     print(f"{index+1}: {line}",end="")
# infile.close()
# outfile.close()
# print("\ncopied successfully")







###10
# filename = input("Enter the file name: ").strip()
# infile = open(filename, "r")

# freqs = {}

# # Extract each character and count it.
# for line in infile:
#     for char in line.strip():
#         if char in freqs:
#             freqs[char] += 1;
#         else:
#             freqs[char] = 1
# print(freqs)
# infile.close()







###11
# key = 'abcdefghijklmnopqrstuvwxyz'

# # Recieves plaintext, encrypts it and returns ciphertext

# def encrypt(n,plaintext):
#     result = ''
    
#     for l in plaintext.lower():
#         try:
#             i = (key.index(l)+n)%26
#             result += key[i]
#         except ValueError:
#             result += l;
    
#     return result.lower()

# # Receive the ciphertext, decrypt it, and return the plaintext.
# def decrypt(n,ciphertext):
#     result = ''
    
#     for l in ciphertext:
#         try:
#             i = (key.index(l)+n)%26
#             result += key[i]
#         except ValueError:
#             result += l;
    
#     return result

# n = 3
# text = "The language pf truth is simple"
# encrypt = encrypt(n,text)
# decrypt = decrypt(n,encrypt)
# print("Text: ",text)
# print("encrypt: ",encrypt)
# print("decrypt: ",decrypt)






###12


# with open('proverb.txt','r') as f:
#     str = f.read()
#     print(str)
#     # file automatically closes after the with block




###13
# lines = ["we'll find a way, we'll find a way\n",
#          "I'll find you a way and I'll kill you\n",
#          "I'll be back Terminator2\n"]

# with open('movie-quotes.txt','w') as f:
#     for line in lines:
#         f.write(line)
#     print("Written was successfully")





###14
# lines = ["we'll find a way, we'll find a way\n",
#          "I'll find you a way and I'll kill you\n",
#          "I'll be back Terminator2\n"]

# with open('movie-quotes.txt','w') as f:
#     f.writelines(lines)
#     print("Written was successfully")