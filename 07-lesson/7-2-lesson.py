# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 06:30:25 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: Tuple, Dict, Str, Set and List
"""

###1
# numbers = {2,1,3}
# print(numbers)
# print(len(numbers))

# fruits = {"Apple", "Banana", "Pineapple"}
# mySet = {1.0, 2.0, "Hello World", (1,2,3)}

# print(fruits)
# print(mySet)






###2
# numbers = {2,1,3,4}
# print(numbers)
# if 1 in numbers:
#     print(f"There is {1} in numbers.")


# for x in numbers:
#     print(x, end=" ")





###3
# myset = set("zokirkhon")
# print('o' in myset)
# print('a' in myset)
# print(myset)





###4
# setss = {1,2,"kkc",[1,3,5],(6,7,8)}
# print(setss) # TypeError: unhashable type: 'list'
# set1 = {1,2,"kkc",(6,7,8)}
# print(set1)
# set2 = {2,5,6,2,4,3,5}
# print(set2)



###5
# for x in {2,3,"kkc"}:
#     print(x)

# for x in {2,3,1}:
#     print(x)

# for x in {'k',3,1,(1,2)}:
#     print(x)

# results are different


###6
# num = set([1,2,3])
# print(num)

# num2 = set([1,2,3,1,2,5,6,7,8,6])
# print(num2)

# num3 = set((1,2,3))
# print(num3)

# num4 = set("zokirkhon")
# print(num4)






###7
# set1 = set('banana')
# print(set1)

# for char in set("zokirkhon"):
#     print(char)





###8
# numbers = {1,2,3}
# numbers.add(4) ###add
# print(numbers)





###9
# num = {2,4,'kkc'}
# print(num)
# # num.update(6,7) 'int' object is not iterable
# num.update([6,7])
# print(num)
# num.discard(6) ###discard
# print(num)
# num.update((10,11)) ###update
# print(num)
# num.remove(7) ###remove
# print(num) 
# # num.remove(1) ### KeyError: 1
# num.clear() ###clear
# print(num)





###10
"""
| : union
& : intersection
- : difference
^ : Symmetry difference

"""
# x = {2,3,2,3,4,5,1}
# y = {3,4,5,6,7}
# print(x | y)
# print(x & y)
# print(x - y)
# print(x ^ y)




###11
# a = {1,2,3}
# b = {1,2,3}
# print(a==b)
# a = {1,2,3,4,5}
# b = {1,2,3}
# print(a>b)
# print(b.issubset(a))
# print(a.issuperset(b))






###12
# a = {1,2,3}
# b = {3,4,5}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
# print(a.union(b))
# print(b.union(a))
# print(a.intersection(b))
# print(b.intersection(a))
# print(a.difference(b))
# print(b.difference(a))






###13
"""
List of people who attended the old party are stored in sets A and B, respectively.
How do I print out list of people who attended both parties?

output: Thoso who attended both parties were: "Zokirkhon", "Sayfullokhon"

"""
# partyA = set(["Zokirkhon", "Abdulkhamid","Khurshidbek","Sayfullokhon"])
# partyB = set(["A'zamjon","Murodillo Oka","Zokirkhon","Sayfullokhon"])
# print("Thoso who attended both parties were: ", end=" ")
# print(partyA.intersection(partyB))
# print(partyA & partyB)







###14
"""
Let's write a program that reads a text file and counts how many words are used to create a document.

Input file name: proverbs.txt
Number of words used: 20

{"travels","half","that","news","alls","well","fast","feather","flock","bad",
"together","end","is","a","done","begun","birds","of","the","name"}

"""

# Remove punctuation from words and make them lowercase.
def allWord_lowerMaker(word):
    output = '';
    for character in word:
        if character.isalpha():
            output += character
    return output.lower();

words_set = set()

# Open the file.
file_name = input("Input file name: ")
file = open(file_name, "r")

# Repeat for every line in the file.
for line in file:
    line_words = line.split()
    for each_word in line_words:
        words_set.add(allWord_lowerMaker(each_word)); # add the word to set
print(f"Number of words used: {len(words_set)}")
print(words_set)
