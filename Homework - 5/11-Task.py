# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:21:18 2021

@author: Zokirkhon
task: 11. Write the execution result of smart_base1.py executed by importing phone_base.py and camera_base.py modules.
"""
import camera_base
#import phone_base
# we need to import the phone_base in order to use the makeCall() function
print("-"*10)
camera_base.photo()

phone_base.makeCall()
phone_base.makeCall()

#output: 
""" Taking a photo...
----------
Taking a photo...
Traceback (most recent call last):
  File "11-Task.py", line 12, in <module>
    phone_base.makeCall()
NameError: name 'phone_base' is not defined
"""



