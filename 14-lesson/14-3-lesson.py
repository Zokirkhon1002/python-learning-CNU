# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:23:14 2021

@author: Zokirkhon
@topic: handling files and exceptions
"""



###1
# print(bin(123456))









###2
# outfile = open("new.txt","wb")
# bytes = bytes([255,128,0,1])
# print(bytes)
# outfile.write(bytes)
# outfile.close()
# print("done")








###3
# outfile = open("new.txt","rb")
# for line in outfile.read():
#     print(line)
# outfile.close()







###4
# filename1 = input("Enter the name of the original file: ")
# filename2 = input("Enter the name of the copying file: ")

# infile = open(filename1,"rb")
# outfile = open(filename2,"wb")

# # Read 1024 bytes from input file and write to output file
# while True:
#     copy_img = infile.read(1024)
#     if not copy_img:
#         break;
#     outfile.write(copy_img)

# infile.close()  # Close input file
# outfile.close() # Close output file
# print("Done")









###5
# from pickle import dump, load

# myMovie = {"superman":9.8, "batman":9.6, "spiderman":9.5, "ironman":9.4}

# dump(myMovie, open("save.p",'wb'))

# myMovie = load(open('save.p','rb'))
# print(myMovie)






