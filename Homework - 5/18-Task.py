# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:20:42 2021

@author: Zokirkhon
task: 18. Describe the program below code.
"""



filename1 = input("원본 파일 이름을 입력하시오: "); 
# input file name

filename2 = input("복사 파일 이름을 입력하시오: "); 
# input file name second

infile = open(filename1,'rb') 
# Use the 'rb' mode in the open() function to read a binary files, as shown below.

outfile = open(filename2, "wb") 
# Use the 'wb' mode in the open() function to write a binary files, as shown below.

while True: 
    # Loop until the end of the file.
    
    copy_buffer = infile.read(1024) 
    # Read 1024 bytes at a time.
    
    print(copy_buffer) 
    # print the copy_buffer
    
    if not copy_buffer: 
        # if copy_buffer is empty
        
        break # break the loop
    
    outfile.write(copy_buffer) 
    # write the copy_buffer to the outfile
    
infile.close() # close the infile 
outfile.close() # close the outfile 

print(filename1+"를 " +filename2+"로 복사하였습니다. ") 
#output: "filename1" is copied to "filename2"

# output:
# 원본 파일 이름을 입력하시오: 18-image.png
# 복사 파일 이름을 입력하시오: image.txt
# 18-image.png를 image.txt로 복사하였습니다. 
