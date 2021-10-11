# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:37:16 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


"""
English:

To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string 
that is surrounded by double quotes:


Korean:

문자열에 잘못된 문자를 삽입하려면 이스케이프 문자를 사용하십시오.
이스케이프 문자는 백슬래시 \ 뒤에 삽입하려는 문자가 오는 것입니다.
잘못된 문자의 예로는 큰따옴표로 묶인 문자열 안의 큰따옴표가 있습니다.

"""

# It will get an error if you use double quotes inside a string that is surrounded by double quotes:
# 큰따옴표로 묶인 문자열 안에 큰따옴표를 사용하면 오류가 발생합니다.

txt = "Chonnam national university, short form is "CNU"."
txt = 'Chonnam National University, short form is 'CNU'.'


# To fix this problem, use the escape character \":
# 이 문제를 해결하려면 이스케이프 문자 \":를 사용하십시오.



txt = "Chonnam national university, short form is \"CNU\"."
txt = 'Chonnam National University, short form is \'CNU\'.'

"""
English:

Other escape characters used in Python:


Korean:

Python에서 사용되는 기타 이스케이프 문자:
"""


"""
\'  Single Quote 
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""



























