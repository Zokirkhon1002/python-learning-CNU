# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:16:35 2021

@author: Zokirkhon
topic: handling files and exceptions
"""


# 1
# infile = open('1.js', 'r')
# print(infile.read())


# 2
# infiles = open('phone.txt', 'w')
# infiles.write('Zokirkhon 010-1234-5678')
# infiles.write('\nZokirkhon 010-1234-5678')
# infiles.write('\nZokirkhon 010-1234-5678')
# print("Successfully write to file")


# 3
# infile = open('phone.txt', 'r')
# print(infile.read())
# infile.close()
# infile = open('phone.txt', 'r')
# print(infile.readlines())
# infile.close()


# 4
# infile = open('phone.txt', 'r')
# s=infile.readline()
# print(s, end='')
# s=infile.readline()
# print(s)
# s=infile.readline()
# print(s)
# infile.close()
# infile = open('phone.txt', 'r')
# ch=infile.read(10)
# print(ch)
# ch=infile.read()
# print(ch)


# 5
# infile = open('phone.txt', 'r')
# line = infile.readline()
# while line != "":
#     print(line);
#     line = infile.readline()
# infile.close()


# 6
# infile = open('phone.txt', 'r')
# for line in infile:
#     line = line.rstrip()
#     print(line)
# infile.close()


# 7
# infile = open('phone.txt', 'r')
# line = infile.readlines()
# print(line)
# infile.close()


# 8
# infile = open('phone.txt', 'r')
# print(infile)

# print("-------")
# line1 = infile.read()
# print(line1)
# print("$$$$$")
# for i in infile:
#     print(i)

# print("#######")
# line2 = infile.read()
# print(line2)

# print("@@@@@@@")
# infile.seek(10)
# line2 = infile.read()
# print(line2)
# infile.close()


# 9
# outfile = open('w-phones.txt', 'w')

# outfile.write('Zokirkhon 010-1234-5678')
# outfile.write('\nKhan Media 010-1234-5678')
# outfile.write('\nXan 010-1234-5678')
# outfile.close()


### 10
# import os

# outfile = open('w2-phones.txt', 'w')
# if os.path.isfile('w2-phones.txt'):
#     print('file exists')
# else:
#     outfile.write('Zokirkhon 010-1234-5678')
#     outfile.write('\nKhan Media 010-1234-5678')
#     outfile.write('\nXan 010-1234-5678')
# outfile.close()







###11
# str_list = ['Zokirkhon\n', 'Khan Media\n', 'Xan']
# f=open('w3-phones.txt', 'w')
# f.write('Zokirkhon\n')
# f.writelines(str_list)
# f.close()







###12
# Get the input file name and output file name from the user
infilename = input('Enter the input file name: ')
outfilename = input('Enter the output file name: ')

# Open files for input and output
infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

# Define variables for sum and count
sum,count=0,0;

# Read a line from the input file and compute the sum
for each in infile:
    dailySale = int(each)
    sum += dailySale
    count += 1

# Record total sales and daily average sales to the output file
outfile.write('Total sales: ' + str(sum) + '\n')
outfile.write('Average daily sales: ' + str(sum/count))

infile.close()
outfile.close()
print('Done!')