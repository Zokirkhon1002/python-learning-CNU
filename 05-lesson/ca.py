# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:10:22 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""


# Command_arguments: ca.py

print("Test Program")
from sys import argv

if __name__ == '__main__':
    print(f"Number of argv: {len(argv)}")
    for eachItem in argv:
        print(eachItem)