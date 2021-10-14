"""
Created on Tue Oct 12 21:24:07 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


# Task:
# Describe the following program and write the output.

def sub():
    global s
    print(s)
    s = "Banana is good"
    print(s)
s = "Apple is good"
sub();
# print(s)

# Output
# Value of s inside a function: Apple is good
# Value of s inside a function: Banana is good
# Value of s outside a function: Banana is good



""" 
English:

In the above example, we first define 's' as global keyword inside the function sub().
then we printed in console
The value of 's' is then defined as "Banana is good" then printed again.
outside the function, we firstly defined 's' as "Apple is good".
After we call sub() function, we printed 's' outside a function.


Korean:

위의 예에서 우리는 먼저 's'를 함수 sub() 내에서 전역 키워드로 정의합니다.
그런 다음 콘솔에서 인쇄했습니다.
그런 다음 'Banana is good'으로 값을 정의한 다음 다시 인쇄합니다.
함수 외부에서 먼저 'Apple is good'으로 정의했습니다.
sub() 함수를 호출한 후 함수 외부에 's'를 인쇄했습니다.
"""