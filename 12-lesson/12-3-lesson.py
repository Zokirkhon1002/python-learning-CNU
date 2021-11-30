# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:42:13 2021

@author: Zokirkhon
"""

###1
#os module
import os
import random
# print(os.name)
# print(os.getcwd())





# print(os.getcwd())
# print(os.chdir("D:\\Coding Class\\Self study from Videos\\Python programming\\Chonnam National University\\12-lesson"))



# print(os.path.join(os.getcwd(), "12-3-lesson.py"))
# print(os.path.join("D:\\Coding Class\\Self study from Videos\\Python programming\\Chonnam National University\\12-lesson", "12-3-lesson.py"))








# for i in os.listdir(os.getcwd()):
#     print(i)


# making a new folder
# os.mkdir(os.path.join(os.getcwd(), "12-3-lesson"))
# os.mkdir(os.path.join(os.getcwd(), "12-4-lesson"))


# removing a file
# os.remove(os.path.join(os.getcwd(), "12-4-lesson"))

# removing a folder
# os.removedirs(os.path.join(os.getcwd(), "12-4-lesson"))

# print(os.system("dir"))



# print(os.system("calc"))




# print(os.listdir("."))



# print(os.mkdir("myfiles"))
# print(os.listdir("."))




import sys

# print(sys.prefix)

# print(sys.path)

# print(sys.version)





import time

# if __name__ == "__main__":
#     t1 = time.time()
#     print(t1)
    
#     t2 = time.gmtime()
#     print(t2)
#     # output:
#     # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=25, tm_hour=15, tm_min=42, tm_sec=21, tm_wday=6, tm_yday=321, tm_isdst=0)
    
#     t3 = time.localtime()
#     print(t3)
#     # output:
#     # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=25, tm_hour=15, tm_min=42, tm_sec=21, tm_wday=6, tm_yday=321, tm_isdst=0)







# if __name__ == '__main__':
#     input("Press Enter to continue...")
#     t1 = time.time()
    
#     time.sleep(5) # sleep for 5 seconds
#     input("Press Enter to continue...")
    
#     t2 = time.time()
#     time_gap = t2 - t1
#     print(f"Time gap: {time_gap}")










# print(f"Year: {time.strftime('%Y',time.localtime())}")
# print(f"Month: {time.strftime('%m',time.localtime())}")
# print(f"Date: {time.strftime('%d',time.localtime())}")
# print(f"day: {time.strftime('%A',time.localtime())}")



import datetime

# print(datetime.date.fromtimestamp(time.time()))
# output: 2020-11-25




# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=" ")
#         a, b = b, a+b
#     print()

# start = time.time()
# fib(1000000000000000000000000000000000000)
# end = time.time()
# print(f"Time taken: {end-start}")










import calendar

# def cal(n):
#     while n > 0:
#         print(calendar.month(2021, n))
#         n -= 1
# cal(12)








###Games with Python
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    response = input("Continue tossing the coin?(yes,no): ");
    if response == "no":
        print("Game over")
        break
    else:
        print(random.choice(myList))