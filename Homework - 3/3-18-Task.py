"""
Created on Fri Oct 15 01:41:13 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""


# Task:
# Describe the following program and write the output

scores = {"Korean":80, "Math":90,"English":80}
# we create dictionary for collecting data.
# 데이터 수집을 위한 사전을 만듭니다.

for item in scores.items():
    
    # we used items() method for dictionary. Items() method can iterate key-value pairs.
    # It can also be received as a tuple of (key, value).
    # we used  as a tuple of (key, value) in this section
    
    # 사전에 items() 메서드를 사용했습니다. Items() 메서드는 키-값 쌍을 반복할 수 있습니다.
    # (key, value)의 튜플로 받을 수도 있습니다.
    # 이 섹션에서 (키, 값)의 튜플로 사용했습니다.
    
    print(item)
    
    # And we printed each item
    # 그리고 우리는 각 항목을 인쇄했습니다.
    

# output
# ('Korean', 80)
# ('Math', 90)
# ('English', 80)