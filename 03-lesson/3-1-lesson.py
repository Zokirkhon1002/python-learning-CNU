# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:08:14 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI
"""

# # 1
# score = int(input("Please enter your score\n>>> "))
# if score >= 60:
#     print("you are passed")
# else:
#     print("you are not passed")


# # 2
# a = 3 > 2
# print(a)
# a = 2 > 3
# print(a)



# # 3
# age = int(input("Please enter your age\n>>> "))
# if (age >= 19):
#     print("you are able to buy Alcoholic beverages at the super market")
# else:
#     print("Your age is not enough, please wait a bit.")


# # 4
# food = input("Please enter your favourite food\n>>> ")
# if food == "steak":
#     print("My Favourite food!")
#     print((food + '\t') * 10 )


# # 5
# isSnowing = input("is it snow/rain? (yes/no)\n>>> ")
# if isSnowing.lower() == 'yes':
#     hasUmbrella = input("do you have an Umbrella? (yes/no) \n>>> ")
#     if hasUmbrella.lower() == 'yes':
#         print("if go out, please get your umbrella")
#     else:
#         print("please wait in your home, untill rain/snow stops")
# else:
#     print("you can go out:)")



# # 6
# import turtle
# t=turtle.Pen()

# while True:
#     direction = input("left, right, red, green, blue, yellow, purple, black, forward:")
#     if direction == 'left':
#         t.left(60)
#         t.forward(50)
#     if direction == 'right':
#         t.right(60)
#         t.forward(50)
#     if direction == 'green':
#         t.pencolor("green")
#     if direction == 'red':
#         t.pencolor("red")
#     if direction == 'blue':
#         t.pencolor("blue")
#     if direction == 'black':
#         t.pencolor("black")
#     if direction == 'yellow':
#         t.pencolor("yellow")
#     if direction == 'purple':
#         t.pencolor("purple")
#     if direction == 'forward':
#         t.forward(100)




# # 7
# weight = float(input("How much is the weight of the load?\n>>> "))
# if weight > 20:
#     print("for heavy luggage, you must pay 20 000won")
# else:
#     print("There is no fee for luggage")
# print("Thank you very much!")






# # 8
# number = int(input("Please input the number\n>>> "))
# print("this is even numbers") if number%2==0 else print("this is odd numbers");



# # 9 return max
# nums = []
# for i in range(2):
#     nums.append(int(input(f"Please enter {i+1}-number\n>>> ")))

# print(f"max number is {nums[0]}") if nums[0] > nums[1] else print(f"max number is {nums[1]}")





# # 10
# score = int(input("Please enter your score\n>>> "))
# if score >= 90:
#     print("you are passed")
#     print('you can al get scholarship')





# # 11
# sales = int(input("Please enter you paid momey\n>>> "))
# if sales >= 1000:
#     discount = sales*0.1
#     print(discount, "You received discount!")
# else:
#     if sales > 500:
#         discount = sales*0.05
#         print(discount, "You received discount!")
#     else:
#         print("There is not discount")





# # 12
# paidMoney = int(input("Please enter you paid momey\n>>> "))
# if paidMoney >= 100_000:
#     discount = paidMoney*0.05
#     sales = paidMoney-discount
# print(f"Payment is amount {sales}")







# # 13
# string = input("Please enter a word\n>>> ")
# length = len(string)
# half = length // 2
# if length%2==1:
#     print(f"middle character is: {string[half]}")
# else:
#     print(f"middle character is: {string[half-1]} {string[half]}")








# # 14
credits = float(input("Please enter your Credits\n>>> "))
gpa = float(input("Please enter your GPA\n>>> "))
if (credits >= 140) and (gpa >= 2.0):
    print("Gradutaion is possible")
else:
    print("Graduation is difficult")