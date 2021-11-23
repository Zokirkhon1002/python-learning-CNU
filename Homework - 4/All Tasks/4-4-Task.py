# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:15:18 2021

@author: Zokirkhon
Homework - 4.4
"""


"""
Task: Write the result of the following program
직무: 다음 프로그램의 결과를 쓰시오
"""

class Counter:
    count=0;
    def reset(self):
        self.count=0;
    def increment(self):
        self.count +=1;
    def get(self):
        return self.count
a=Counter();
print(a.get())
# output: 0;

a.reset()
a.increment()
print(a.get())
# output: 1