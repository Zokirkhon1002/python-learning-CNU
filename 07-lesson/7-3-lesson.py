# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:01:58 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

Theme: Tuple, Dict, Str, Set and List
"""




###1
# contacts = {
#     "Zokirkhon":"01080891816",
#     "Abdulkhamid":"998975661718",
#     "Sayfullokhon":"01058912026",
#     "Khurshidbek":"998999330348",
#     "Bobur":"998913430668",
# }
# print(contacts)





###2
# a = 77
# b = [1,2,3]
# c = 'Python'
# # dic_test = {a:b,b:c,c:a} # TypeError: unhashable type: 'list'
# # Dictionary can't read list as a key. But can read list as a value.
# dic_test = {a:b,tuple(b):c,c:a}
# print(dic_test)






###3
# contacts = {
#     "Zokirkhon":"01080891816",
#     "Abdulkhamid":"998975661718",
#     "Sayfullokhon":"01058912026",
#     "Khurshidbek":"998999330348",
#     "Bobur":"998913430668",
# }

# print(contacts['Zokirkhon'])
# print(contacts['Bobur'])

# if "Zokirkhon" in contacts:
#     print("Key is in the dictionary")





###4
# contacts = {
#     "Zokirkhon":"01080891816",
#     "Abdulkhamid":"998975661718",
#     "Sayfullokhon":"01058912026",
#     "Khurshidbek":"998999330348",
#     "Bobur":"998913430668",
# }
# print(contacts.get("Ali", "There is not Ali name as key"))






###5
# scores = {
#     "Korean":80,
#     "Math":90,
#     "English":90,
# }
# print(scores.keys())
# print(scores.values())
# print(scores.items())





###6
# scores = {
#     "Korean":70,
#     "Math":90,
#     "English":90,
# }
# scores['Turkish'] = 70;
# scores['Arabic'] = 50;
# print(scores)

# arabic = scores.pop("Math")
# print(scores)
# print(arabic)





###7
# scores = {
#     "Korean":70,
#     "Math":90,
#     "English":90,
#     'Turkish':70,
# }
# print(scores)
# scores.update({'Frontend':95,"Turkish":60})
# print(scores)
# del scores; ### All informations deleted
# print(scores)







###8
# scores = {
#     "HTML":90,
#     "CSS":80,
#     "JavaScript":95,
#     "Bootstrap":85,
#     "Material css":80,
#     "Sass":80,
#     "ReactJS":80,
#     "Python":50,
# }
# print(list(scores))







###9
# test = ['ab','cd','ef']
# print(dict(test))







###10
# scores = {
#     "HTML":90,
#     "CSS":80,
#     "JavaScript":95,
#     "Bootstrap":85,
#     "Material css":80,
#     "Sass":80,
#     "ReactJS":80,
#     "Python":50,
# }
# for items in scores.items():
#     print(items)
# for key in scores.keys():
#     print(key)
# for value in scores.values():
#     print(value)





###11
# dict1 = {x:x*x*x for x in range(1,6)}
# print(dict1)







###12
# scores = {
#     "HTML":90,
#     "CSS":80,
#     "JavaScript":95,
#     "Bootstrap":85,
#     "Material css":80,
#     "Sass":80,
#     "ReactJS":80,
#     "Python":50,
# }
# print(sorted(scores))
# print(sorted(scores.values()))
# print(dir(scores))







###13
# scores = {
#     "HTML":90,
#     "CSS":80,
#     "JavaScript":95,
#     "Bootstrap":85,
#     "Material css":80,
#     "Sass":80,
#     "ReactJS":80,
#     "Python":50,
# }
# print(sorted(scores,key=scores.__getitem__))
# print(sorted(scores,key=scores.__getitem__, reverse=True))






###14
"""
Let us implement an English-Korean dictionary. 
How can I do it? You can create a blank dictionary and store it with an English word
as a key and a description as a value.

input: Enter a word: one
output: 하나

input: Enter a word: Python
output: Unknown word.

"""
# def english_dic(word):
#     english_words_dic = {'one':"하나",'two':"둘",'three':"셋"};
#     print(english_words_dic.get(word,'Unknown word.'))

# word = input("Enter a word: ").lower()
# english_dic(word)







###15
"""
Older people often use abbreviations. For example: 
There are abbreviations such as:
"B4(Before)" "TX(Thanks)" "BBL(Be Back Later)" "BCNU(Be Seeing You)"
"HAND(Have A Nice Day)". Let's write a program that unpacks 
abbreviations and converts them into general sentences.


input: Please enter the sentence to be translated: TX Mr. Park!
Output: Thanks Mr.Park!.

"""

def abbr(msg):
    table = {
        "B4": "Before", 
        "TX": "Thanks", 
        "BBL": "Be Back Later", 
        "BCNU" : "Be Seeing You " , 
        "HAND":"Have A Nice Day",
    }
    result = ''
    each_words = msg.split()
    for each_word in each_words:
        if each_word in table:
            result += table[each_word] + " "
        else:
            result += each_word;
    print(result)

message = input("Please enter the sentence to be translated: ")
abbr(message)

