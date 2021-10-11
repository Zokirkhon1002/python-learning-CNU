# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:49:54 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
"""
writing a program that simulates a vending machine.
User can use 1000 won banknote, 500 won coins, 100 coins.
If you enter the price of an item and the number of 1000 won banknote,
500 won coins and 100 won coins, change is calculated and returned in coins.
"""




itemPrice = int(input("enter price of item: \n>>> "))
bankNote10_000 = int(input("enter number of 10 000won banknote: \n>>> "))
bankNote1000 = int(input("enter number of 1000won banknote: \n>>> "))
coin500 = int(input("enter number of 500won coincash: \n>>> "))
coin100 = int(input("enter number of 100won coincash: \n>>> "))



change = bankNote10_000*10000 + bankNote1000*1000 + coin500*500 * coin100*100 - itemPrice


## Calculate the change(number of 1000 bankNote);
resultCoin1000 = change // 1000
change = change % 1000

## Calculate the change(number of 500 coins);
resultCoin500 = change // 500
change = change % 500


## Calculate the change(number of 100 coins);
resultCoin100 = change // 100
change = change % 100


## Calculate the change(number of 10 coins);
resultCoin10 = change // 10
change = change % 10


## Calculate the change(number of 1 coins);
resultCoin1 = change

print(f"\n1000won = {resultCoin1000}"
      f"\n500won = {resultCoin500}"
      f"\n100won = {resultCoin100}"
      f"\n10won = {resultCoin10}"
      f"\n1won = {resultCoin1}")