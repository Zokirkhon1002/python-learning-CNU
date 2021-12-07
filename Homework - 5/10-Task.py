# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:14:44 2021

@author: Zokirkhon
task: 10. Describe the following program and write the result.
"""


import time 
# import time module

if __name__ == "__main__": 
    # if this is the main file
    
    t1 = time.time() 
    # get the time
    
    print(t1) 
    # output: 1638756950.7298193
    
    t2 = time.gmtime() 
    # get the time in the format of time.struct_time
    
    print(t2) 
    # output: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=6, tm_hour=11, tm_min=14, tm_sec=14, tm_wday=5, tm_yday=355, tm_isdst=0)
    
    t3 = time.localtime() 
    # get the time in the format of time.struct_time
    
    print(t3)
    # output: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=6, tm_hour=11, tm_min=14, tm_sec=14, tm_wday=5, tm_yday=355, tm_isdst=0)


