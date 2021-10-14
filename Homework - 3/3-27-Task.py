"""
Created on Fri Oct 15 02:55:59 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

#Task:
# Describe the following program
# Selection sort




def selectionSort(aList):
     # i indicates how many items were sorted
     
     # i는 정렬된 항목 수를 나타냅니다.
    for i in range(len(aList)):
        # To find the minimum value of the unsorted segment.
        # We first assume that the first element is the lowest.
        
        # 정렬되지 않은 세그먼트의 최소값을 찾습니다.
        # 먼저 첫 번째 요소가 가장 낮다고 가정합니다.
        least = i
        leastValue = aList[i]
        # We then use k to loop through the remaining elements.
        
        # 그런 다음 k를 사용하여 나머지 요소를 반복합니다.
        for k in range(i+1, len(aList)):
            # Update the least and leastValue if the element at aList[k] is lower than leastValue.
            
            # "aList[k]"의 요소가 "leastValue"보다 낮은 경우 "least" 및 "leastValue"를 업데이트합니다.
            if aList[k] < leastValue:
                least = k
                leastValue = aList[k]

        # After finding the lowest item of the unsorted regions, 
        # swap with the first unsorted item via tmp variable
        
        # 정렬되지 않은 영역 중 가장 낮은 항목을 찾은 후,
        # tmp 변수를 통해 정렬되지 않은 첫 번째 항목으로 교체합니다.
        tmp = aList[i]
        aList[i] = aList[least]
        aList[least] = tmp


list1 = [20,30,90,50,10,70,80]
selectionSort(list1)
print(list1)


#  Output
# [10, 20, 30, 50, 70, 80, 90]
