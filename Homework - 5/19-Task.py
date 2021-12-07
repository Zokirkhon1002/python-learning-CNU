# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:43:34 2021

@author: Zokirkhon
task: 19. Describe the program below and write the result.
"""

import pickle
# pickle is a module that can serialize and deserialize Python objects to and from a binary stream.

myMovie = {"Superman vs Batman ": 9.8, "Ironman": "9.6"} 
# dictionary


pickle.dump(myMovie, open("save.p", "wb"))
# pickle.dump is a function that serializes the object passed to it and saves it to the file specified by the filename parameter.
# open(filename, 'wb') wb is write binary

myMovie = pickle.load(open("save.p", "rb")) 
# pickle.load is a function that loads the object that was saved to the file specified by the filename parameter.
# open(filename, 'rb') rb is read binary

print(myMovie)
# ouput: {'Superman vs Batman ': 9.8, 'Ironman': '9.6'}
