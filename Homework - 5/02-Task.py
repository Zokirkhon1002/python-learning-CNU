# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:29:00 2021

@author: Zokirkhon

task: 2. Describe the following program and write the result.
"""

numbers = [2,3,1,5,4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# output: [1, 2, 3, 4, 5]



"""
English:

sorted() function sorts the list in ascending order.
Return a new sorted list from the items in iterable.
Has two optional arguments which must be specified as keyword arguments.
key specifies a function of one argument that is used to extract a comparison key 
from each element in iterable (for example, key=str.lower). 
The default value is None (compare the elements directly).
reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.



Korean:

sorted() 함수는 목록을 오름차순으로 정렬합니다.
iterable의 항목에서 새로운 정렬된 목록을 반환합니다.
키워드 인수로 지정해야 하는 두 개의 선택적 인수가 있습니다.
키는 비교 키를 추출하는 데 사용되는 한 인수의 함수를 지정합니다.
iterable의 각 요소에서 가져옵니다(예: key=str.lower).
기본값은 없음(요소를 직접 비교)입니다.
reverse는 부울 값입니다. True로 설정하면 목록 요소가 각 비교가 반대로 된 것처럼 정렬됩니다.
"""