# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:39:26 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: List
"""


# 1
# list1 = [3,4,5]
# list2 = [x*2 for x in list1]
# print(list2)


# 2
# M = [x for x in range(10) if x % 2 == 0]
# print(M)


# 3
# word_list = "Doncount your chickens before they are hatched".split()
# result_list = [len(word) for word in word_list]
# print(result_list)


# 4
# colors = ["white", "black", "silver"]
# cars = ["Hyundai","Sonata","Malibu","Avante"]
# colored_cars_dic = [{x:y} for x in colors for y in cars]
# colored_cars = [(x,y) for x in colors for y in cars]
# print(colored_cars)
# print(colored_cars_dic)


# 5
# new_list = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
# print(new_list)
# ### with regular way
# new_list2 = []
# for x in range(1,30):
#     for y in range(x,30):
#         for z in range(y,30):
#             if x**2 + y**2 == z**2:
#                 new_list2.append((x,y,z))

# print(new_list2)


# 6
# numbers = [100,20,40,60,30,50]
# minimum = numbers[0]

# for i in range(1,len(numbers)):
#     if (numbers[i] < minimum):
#         minimum = numbers[i];

# print(minimum)


# 7
# numbers = [100,20,40,60,30,50]
# maximum = numbers[0]

# for i in range(1,len(numbers)):
#     if (numbers[i] > maximum):
#         maximum = numbers[i];

# print(maximum)


# 8
# words = ['cat','puppet','elephent','tiger','rabbit']
# shortest = words[0]

# for i in range(1,len(words)):
#     if len(words[i]) < len(shortest):
#         shortest = words[i]
# print(shortest)


# 9
# words = ['cat','puppet','elephent','tiger','rabbit']
# longest = words[0]

# for i in range(1,len(words)):
#     if len(words[i]) > len(longest):
#         longest = words[i]
# print(longest)


# 10
# Sequential search

# def linear_Search(list,search_item):
#     for i in range(len(list)):
#         if search_item == list[i]:
#             return i;
#     return -1

# numbers = [10,20,30,40,50,60,60]
# position = linear_Search(numbers,50)

# if position != -1:
#     print(f"Success: Position = {position}, item is: {numbers[position]}")
# else:
#     print("Fail")

# Return the index of search_item


# 11
# numbers = [100,20,30,40,50,60,70,80,90,32,33]
# result = []

# for each in numbers:
#     if each > 50:
#         result.append(each)

# print(result)


# 12
# Selection sort
# def selectionSort(list):
#     for i in range(len(list)):
#         least = i
#         leastValue = list[i]

#         for j in range(i+1, len(list)):
#             if list[j] < leastValue:
#                 least = j
#                 leastValue = list[j]


#         temporary = list[i]
#         list[i] = list[least]
#         list[least] = temporary

# list1 = [20,30,40,50,90,50,10,70,80,30]
# selectionSort(list1)
# print(list1)


# 13
# menu = 0
# friends = []
# while menu !=9:
#     print("-"*20)
#     print("1. Print friends list")
#     print("2. Add friend")
#     print("3. Delete friend")
#     print("4. Rename")
#     print("9. End")
#     menu = int(input("Choose a menu: "))
#     if menu == 1:
#         print(friends)
#     elif menu == 2:
#         name = input("Enter a name: ")
#         friends.append(name)
#     elif menu == 3:
#         print(friends)
#         del_name = input("Enter a name you want to delete: ")
#         if del_name in friends:
#             friends.remove(del_name)
#         else:
#             print("Name not found!")
#         # print(friends)
#         # print(range(len(friends)))
#         # delete_friend = int(input("Enter a number: "))
#         # del friends[delete_friend]
#     elif menu == 4:
#         old_name = input("Enter a name you want to change: ")
#         if old_name in friends:
#             index = friends.index(old_name)
#             new_name = input("Enter new name: ")
#             friends[index] = new_name;
#         else:
#             print("Name not found")
# print("the program ended!")


# 14

# s = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]
# print(s)




###15
# rows = 3
# cols = 5

# s =[]

# for row in range(rows):
#     s +=[[0]*cols]
# print(f"s = {s}")






###16
# s = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]

# rows = len(s)
# cols = len(s[0])

# for r in range(rows):
#     for c in range(cols):
#         print(s[r][c], end=',')
#     print()







###17
# aa = [
#     [1,2,3,4],
#     [5,6],
#     [7,8,9]
#     ]
# rows = len(aa)

# for r in range(rows):
#     cols = len(aa[r])
#     for c in range(cols):
#         print(aa[r][c], end=',')
#     print()






###18
### qo'shuv jadvali
# rows = 6
# cols = 6
# table = []

# # # Create a new two-dimensional list.

# for row in range(rows):
#     table += [[0]*cols]

# # # Add the values of rows and cols to each element of the new two-dimensional list and store it.

# for row in range(rows):
#     for col in range(cols):
#         table[row][col] = (row+1+col+1)

# print(table)





###19
board = [[' ' for x in range(3)] for y in range(3)]

while True:
    ### let go and draw the game board.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|  " + board[r][2])
        
        if(r != 2):
            print("---|---|---")
    
    
    #Coordinates are input from the new user.
    x = int(input("Enter the following x numeric coordinates: "))
    y = int(input("Enter the following y numeric coordinates: "))
    
    
    # Inspect the coordinates entered bu the user.
    if board[x][y] != " ":
        print("\n'''Wrong location!''' \n")
        continue
    else:
        board[x][y] = "X"
    
    
    # decide where to put the computer. Place it on the first empty space it finds.
    done = False;
    for i in range(3):
        for j in range(3):
            if board[i][j] == " " and not done:
                board[i][j] = "O";
                done=True;
                break;
    