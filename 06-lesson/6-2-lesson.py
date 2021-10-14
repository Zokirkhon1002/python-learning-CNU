# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:08:42 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: List
"""

###1
# marvel_heros = ["Spiderman", "Hulk", "Ironman"]
# dc_heros = ["Superman", "Betman", "Onedam"]
# heros = marvel_heros + dc_heros;
# print(heros)




###2
# values = [1,2,3]*3
# print(values)




###3
# letters = ['a','b','c','d']
# print(len(letters))





###4
# shopping_list = []
# shopping_list.append("Banana")
# shopping_list.append("PineApple")
# shopping_list.append("Strawberry")
# print(shopping_list)





###5
# marvel_heros = ["Spiderman", "Hulk", "Ironman"]
# dc_heros = ["Superman", "Batman", "Onedam"]
# heros = marvel_heros + dc_heros;
# if "Batman" in heros:
#     print("Batman is hero")
# print("Batman" in heros)

# index = heros.index("Superman")
# print(index)




###6
# marvel_heros = ["Spiderman", "Hulk", "Ironman"]
# dc_heros = ["Superman", "Batman", "Onedam"]
# heros = marvel_heros + dc_heros;
# print(heros)
# heros.pop(1) # remove with index, default remove from last
# print(heros)
# heros.remove("Superman")
# print(heros)







###7
# lst = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
# print(lst)
# lst.remove(2)
# print(lst)
# lst.remove(2)
# print(lst)
# lst.remove(4)
# print(lst)





###8
# list1 = [1,2,3]
# list2 = [1,2,3]
# print(list1 == list2)
# print(list1 != list2)

# list3 = [2,3,4,5,6]
# list4 = [2,3,4,6,5]
# print(list3 > list4)
# print(list3 < list4)






###9
# values = [1,2,3,4,5,6,7,8,9,10]
# print(min(values))
# print(max(values))







###10
# a = [1,10,5,6,7]
# a.reverse()
# print(a)









###11
# a = [3,2,1,5,4]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)






###12
# x = ['ab','xdf','cd','Acd','Trs','z','abcde']
# x.sort()
# print(x)
# x.sort(key=str.lower)
# print(x)
# x.sort(key=len)
# print(x)





###13
# a = [3,2,1,5,4]
# b = sorted(a)
# print(b)
# c = sorted(b, reverse=True)
# print(c)

# text = "A picture is worth a thousand words.!"
# print(sorted(text.split(), key=str.lower))







###14
# str1 = "Where there is a will, there is a way"
# print(str1.split())
# print(str1.split(','))
# print(str1.split('e'))









###15
# scores =  [10,20,30,40,50]
# values = scores
# values[2] = 100
# print(values)
# print(scores)
# for i in scores:
#     print(i,end=' ')







###16
# scores =  [10,20,30,40,50]
# values = list(scores)
# print(values)
# values[2] = 100
# print(values)
# print(scores)
# another = scores[:]
# print(another)






###17
# from copy import deepcopy as dc

# scores =  [10,20,30,40,50]
# values = dc(scores)
# values[3]=200
# print(scores)
# print(values)






###18
### Immutable argument
# def func1(x):
#     print(f"x= {x}, id= {id(x)}")
#     x=99
#     print(f"x= {x}, id= {id(x)}")


# y = 10
# print(f"y= {y}, id= {id(y)}")
# func1(y)
# print(f"y= {y}, id= {id(y)}")

## Output
## y= 10, id= 2817662610000
## x= 10, id= 2817662610000
## x= 99, id= 2817662801328
## y= 10, id= 2817662610000







###19
### Mutable argument

# def func2(list):
#     print(f"list = {list}, id = {id(list)}, Inside of Function")
#     list[2]=100
#     print(f"list = {list}, id = {id(list)}, Inside of Function")

# values = [0,1,2,3,4,5]
# print(f"values = {values}, id = {id(values)}, Outside of Function")
# func2(values)
# print(f"values = {values}, id = {id(values)}, Outside of Function")





###20
def func3(list):
    list[0] = 99;

values = [0,1,2,3,4,5]
print(values)
func3(values)
print(values)