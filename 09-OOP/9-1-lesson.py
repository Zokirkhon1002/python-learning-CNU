# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:43:00 2021

@author: Kotibkhonovo Zokirkhon Zokhidkhon Ugli
student number: 180421
"""

###1
# class Counter:
#     count = 0
#     def reset(self):
#         self.count = 0;
#     def increment(self):
#         self.count += 1
#     def get(self):
#         return self.count;

# a = Counter();
# a.reset()
# print(f"The value of counter a is: {a.get()}")
# a.increment()
# print(f"The value of counter a is: {a.get()}")






###2
# class Counter:
#     def __init__(self):
#         self.count = 0;
#     def reset(self):
#         self.count = 0;
#     def increment(self):
#         self.count += 1
#     def get(self):
#         return self.count;

# a = Counter();
# a.reset()
# print(f"The value of counter a is: {a.get()}")
# a.increment()
# print(f"The value of counter a is: {a.get()}")





###3
# class Counter:
#     """Enter an integer, is optional."""
#     def __init__(self,initvalue = 0):
#         self.count = initvalue;
#     def reset(self):
#         self.count = 0;
#     def increment(self):
#         self.count += 1
#     def get(self):
#         return self.count;

# a = Counter(100);
# b = Counter();

# print(f"The value of counter a is: {a.get()}")
# print(f"The value of counter b is: {b.get()}")



###4
class TV:
    """Enter some informations for your TV"""
    def __init__(self,channel,volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def show(self):
        print(f"The channel is {self.channel} The volume is {self.volume} and the ON is {self.on}")
    
    def set_channel(self,channel):
        self.channel = channel
    
    def get_channel(self):
        return self.channel
    
    def set_volume(self,volume):
        self.volume = volume
    
    def get_volume(self):
        return self.volume
    
    def set_on(self,on):
        self.on = on
    
    def get_on(self):
        return self.on

t1 = TV(9,10,True)
t1.show()
t1.set_channel(11)
t1.show()






































