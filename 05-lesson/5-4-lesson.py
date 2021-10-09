# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:49:38 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""

# print(dir())



###1
# from fibo import fib as f

# f(1000)

# print(f.__name__)





###2
# import fibo

# fibo.fib(1000)

# print(fibo.__name__)





###3
# import ex_module as first


# print("Hello World!")







###4
def readList():
    nlist = []
    flag = True
    while flag:
        number = int(input("Enter a number: "))
        if number < 0:
            flag = False
        else:
            nlist.append(number)
    return nlist


def processList(nlist):
    nlist.sort()
    return nlist


def printList(nlist):
    for sortedNumber in nlist:
        print(f"record: {sortedNumber}")


def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)

if __name__ == "__main__":
    main()





























