# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 06:54:32 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: Lists
"""


###1
### It can recieves all types of datas
# it_recieves = [1,2,3,14,True,"Hello World", "аббосий", [1,2], ["Zokirkhon",23],(True, "False")]










###2
# scores = []
# lessons = int(input("How many lessons have you studied?\n>>> "))
# for i in range(lessons):
#     scores.append(float(input("Enter your grade: ")))

# print(scores)







###3
# scores = [32,56,64,72,12,37,98,77,59,69]
# print(scores)
# scores[0] = 80
# scores[1] = scores[0]
# print(scores)



# i=2
# number=100
# scores[i] = 10
# scores[i+2] = 20

# if i >= 0 and i<len(scores):
#     scores[i+3] = number
# print(scores)








###4
# scores = [32,56,64,72,12,37,98,77,59,69]
# for each_number in scores:
#     print(each_number)







###5
# print(list("Hello"))
# print(list(["Hello"]))
# print(type(("Hello")))
# print(type(("Hello",)))








###6
# list1 = [12,"dog",180.14]
# list2 = [["Seoul",10],["Tashkent",20],["Istanbul",10],]
# list3 = ["aaa",["bbb",["ccc",["ddd", "eee",45]]]]

# print(list3[1][1][1][1])
# print(list3[1][1][1])
# print(list3[1][1])
# print(list3[1])
# print(list3)










###7
### Average Score and highscored students

# students = int(input("How many students are graded?\n>>> "))
# high_scores = []
# scores = []
# scoreSum = 0
# limit_grade = 80

# for i in range(students):
#     grade = float(input(f"Enter {i+1}-student's grade: "))
#     scores.append(grade)
#     scoreSum +=grade
#     if (grade>=limit_grade):
#         high_scores.append(grade)

# avrg_score = scoreSum/len(scores)
# print(f"average score is {avrg_score}")
# print(f"{len(high_scores)} of students that recieved a score of 80 or higher")







###8
# puppy_names = []
# print("q - is quit")
# count = 0
# while True:
#     count+=1
#     name = input(f"Enter {count}-puppy's name: ")
#     if name == "q" or name == "":
#         break
#     puppy_names.append(name)

# for name in puppy_names:
#     print(name, end=", ")







###9
numbers = [32,56,64,72,12,37,98,77,59,69]
# print(12 in numbers)
# print(12 not in numbers)
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))

print(numbers[3:6])





































