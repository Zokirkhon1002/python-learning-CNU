"""
Created on Fri Oct 15 03:50:47 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

# Describe the following program

s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

rows = len(s)
# Rows of list is: 3
# 목록의 행은 다음과 같습니다. 3
cols = len(s[0])
# Columns of list is: 5
# 목록의 열은 다음과 같습니다. 3

for r in range(rows):
    # this loop iterates 3 times for rows
    # 이 루프는 행에 대해 3번 반복합니다.
    for c in range(cols):
        # this loop iterates 5 times for columns
        # 이 루프는 열에 대해 5번 반복합니다.
        print(s[r][c], end=',')
        # print each number of columns and rows
        # 각 열과 행 수를 인쇄합니다.
    print()
    # this print divides each rows.
    # 이 인쇄는 각 행을 나눕니다.
    