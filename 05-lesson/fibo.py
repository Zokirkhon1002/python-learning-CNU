# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:00:16 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""



def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end=" ")
        a,b = b,a+b
    print()

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
