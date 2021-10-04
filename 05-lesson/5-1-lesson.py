# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:25:07 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""

# # #1
##Function
# print(abs(-100))









# # #2
# def get__sum(start,end):
#     """This function recieves 2 parametr, START and END,
#         and returns sum of from START till the END"""
#     sum = 0
#     for i in range(start, end+1):
#         sum += i;
#     return sum

# print(get__sum(1,100))









# # #Power
# def power(number,power):
#     """ Return the value of the base expression taken to a specified power"""
#     result = 1
#     for i in range(power):
#         result *= number
#     return result


# print(power(2,1))
# print(power(2,2))
# print(power(2,3))
# print(power(2,4))
# print(power(2,5))







# # #3
# def say_hello(name):
#     print(f"Hello, {name}")

# say_hello("Zokirkhon")






# # #4
# def say_hello(name,msg):
#     print(f"Hello, {name},  {msg}")

# say_hello("Zokirkhon", "Let's come home")







# # #5
# def get__sum2(end):
#     """This function recieves 1 parametr, END,
#         and returns sum of from 1 till the END"""
#     return int(end*(end/2)+(end/2))
# print(get__sum2(10))







# # #6
# def get_max(x,y):
#     """Return the max from x and y"""
#     if(x>y):
#         return x
#     else:
#         return y
# print(get_max(6,5))
        






# # #7
# def main():
#     print(power(2,4))
#     print(power(2,5))

# def power(number,power):
#     """ Return the value of the base expression taken to a specified power"""
#     result = 1
#     for i in range(power):
#         result *= number
#     return result

# main()






# # #8
# def happyBirthday():
#     """Returns "Happy Birthday!" """
#     print("Happy Birthday!")
#     print("Happy Birthday!")
#     print("Dear My Friend", end=" ")
#     print("Happy Birthday!")

# happyBirthday()








# # #9
# def FtoC(f):
#     """this function returns from Fahrenheit to Celsius"""
#     temp_c = ((f-32)*5)/9
#     return print(temp_c)

# f = float(input("Please enter Fahreheit: \n>>> "))
# FtoC(f)







# # #10
def isPrime(n):
    """Return True if n is prime else False"""
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

n = int(input("Please enter an integer:\n>>> "))
print(isPrime(n))




    







































