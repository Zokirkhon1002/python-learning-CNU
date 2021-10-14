"""
Created on Fri Oct 15 00:29:59 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Task:
# Explane slicing

"""
English:

Python list slicing

To access a range of items in a list, you need to slice a list. 
One way to do this is to use the simple slicing operator :
With this operator you can specify where to start the slicing, where to end and specify the step.
Slicing a List
If L is a list, the expression L [ start : stop : step ] 
returns the portion of the list from index start to index stop, at a step size step


Korean:

파이썬 리스트 슬라이싱

목록의 항목 범위에 액세스하려면 목록을 조각화해야 합니다.
이를 수행하는 한 가지 방법은 간단한 슬라이싱 연산자를 사용하는 것입니다.
이 연산자를 사용하면 슬라이싱을 시작할 위치, 종료 위치 및 단계를 지정할 수 있습니다.
목록 슬라이싱
L이 목록인 경우 표현식 L [ start : stop : step ]
단계 크기 단계에서 인덱스 시작에서 인덱스 중지까지 목록의 일부를 반환합니다.
"""

# Syntax 
# L[start:stop:step]


# 통사론
# L[start:stop:step]

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])
# Prints ['c', 'd', 'e', 'f', 'g']


# Return every 2nd item between position 2 to 7
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])
# Prints ['c', 'e', 'g']
"""
English:

Python String split() Method
Split a string into a list where each word is a list item:


Korean:

파이썬 문자열 split() 메서드
문자열을 각 단어가 목록 항목인 목록으로 분할합니다.
"""

txt = "welcome to the CNU"

x = txt.split()

print(x)

# output
# ['welcome', 'to', 'the', 'CNU'] 



"""
English:
The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.

When maxsplit is specified, the list will contain the specified number of elements plus one.



Korean:

split() 메서드는 문자열을 목록으로 분할합니다.

구분 기호를 지정할 수 있으며 기본 구분 기호는 공백입니다.

maxsplit이 지정되면 목록에는 지정된 수에 1을 더한 요소가 포함됩니다.
"""

# Syntax
# string.split(separator, maxsplit)

# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"




text = "hello, my name is Zokirkhon, I am 23 years old"

y = text.split(", ")

print(y)

# Output
# ['hello', 'my name is Zokirkhon', 'I am 23 years old']
