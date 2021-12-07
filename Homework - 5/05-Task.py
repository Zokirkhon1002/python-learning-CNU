# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:23:55 2021

@author: Zokirkhon
task: 5. Describe the following program and write the result.
"""



"""
English:
    
we cannot copy a list simply by typing lst1 = lst, because: lst1 will only be a reference to lst, 
and changes made in lst will automatically also be made in lst1.


Korean: 

lst1 = lst를 입력하는 것만으로는 목록을 복사할 수 없습니다. lst1은 lst에 대한 참조일 뿐이고,
lst에서 변경한 사항은 lst1에서도 자동으로 적용됩니다.
"""

x = [1, 2, 3] 
# x is a list

lst = [1, 2, x] 
# lst is a list and we wrote x in it

lst1 = lst 
# lst1 is a list and it is equal to lst

print(lst) 
# output: [1, 2, [1, 2, 3]]

print(lst1)
# output: [1, 2, [1, 2, 3]]

lst1[2][1] = 3 
# lst1[2] is a list and we change the second element of it to 3

print(lst1)
# output: [1, 2, [1, 3, 3]]

print(lst)
# output: [1, 2, [1, 3, 3]]

lst1[1] = 3
# lst1[1] is a list and we change the second element of it to 3

print(lst1)
# output: [1, 3, [1, 3, 3]]

print(lst)
# output: [1, 3, [1, 3, 3]]


