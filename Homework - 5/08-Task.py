# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:00:39 2021

@author: Zokirkhon
task: 8. Describe the following program
"""


import os
# os module is used to work with the operating system

# os.getcwd() returns the current working directory
print(os.getcwd())
# output: D:\Coding Class\Self study from Videos\Python programming\Chonnam National University\Homework - 5

# os.chdir() changes the current working directory
print(os.chdir('./'))
# output: None

# os.system() executes the command in the operating system shell
print(os.system('dir'))
# output: 
"""
 Volume in drive D has no label.
 Volume Serial Number is 3663-BA02

 Directory of D:\Coding Class\Self study from Videos\Python programming\Chonnam National University\Homework - 5

12/06/2021  11:00 AM    <DIR>          .
12/05/2021  09:20 PM    <DIR>          ..
12/06/2021  10:10 AM             1,318 01-Task.py
12/06/2021  10:10 AM             1,382 02-Task.py
12/06/2021  10:10 AM               601 03-Task.py
12/06/2021  10:22 AM             2,922 04-Task.py
12/06/2021  10:42 AM             1,142 05-Task.py
12/06/2021  10:51 AM             1,392 06-Task.py
12/06/2021  11:00 AM               975 07-Task.py
12/06/2021  11:04 AM               356 08-Task.py
               8 File(s)         10,088 bytes
               2 Dir(s)  1,934,212,931,584 bytes free
0
"""

