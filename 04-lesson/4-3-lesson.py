# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:37:51 2021

@author: 180421, KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

7-1 Print Function
"""


# # #1
# abc = 'a b c'
# print(1,2,3)
# print('a'+' '+'b'+' '+'c')
# print('%d %d %d'%(1,2,3))
# print('%s %s %s'%('a','b','c'))
# print(f"1 2 3 {abc}")
# print("{} {} {}".format("a","b","c"))









# # #2
# print("%s %s"%("one", "two"))
# print("%d %d"%(1,2))









# # #3
# print("I eat %d apples."%5)
# print("I eat %s apples."%'five')








# # #4
# print("Product: %s, Price per unit: %f"%("Apple", 5.243))









# # #5
# n = 3
# day = 'three'
# print("I ate %d apples. I was sick for %s days"%(n, day))
# # What about this?
# print(f"I ate {n} apples. I was sick for {day} days.")








# # #6
# print("100 + 100")
# print("%d"%(100 + 100))







# # #7
# print("%d"%(100,200))
# print("%d %d"%(200))








# # #8
# print("%d / %d = %d"%(100,200,0.5))
# print("%d / %d = %5.1f"%(100,200,0.5))








# # #9
# print("%d"%123)
# print("%5d"%123)
# print("%05d"%123)







# # #10
# print("%f"%123.45)
# print("%7.1f"%123.45)
# print("%7.3f"%123.45)







# # #11
# print("%s"%'Python')
# print("%10s"%'Python')
# print("%5s"%'Chonnam National University')








# # #12
# print("I'm {0} years old.".format(20))









# # #13
# age,name = 23, 'Zokirkhon'
# print("I'm {0} years old.".format(age))
# print("My name is {0} and {1} years old.".format(name,age))
# print("Product: {0}, Price per unit: {1:.2f}.".format("Apple",5.243))








# # #14
# print("%d %5d %05d"%(123,456,789))
# print("{0:d} {1:5d} {2:05d}".format(123,456,789))








# # #15
# print("{2:d} {1:d} {0:d}".format(123,456,789))








# # #16
# print("{2:d} \b{1:d} \b{0:d}".format(123,456,789))
# print(r"My \n name \t is \b Zokirkhon \\ Kotibkhonov \'Zokhidkhon Ugli\'")








# # #17
# print("%-10.2f"%5.94343)
# print("%10.2f"%5.94343)








# # #18
# print("{0:>10s}".format("Apple"))
# print("{0:<10s}".format("Apple"))









# # #19
# print("{1:10.5f}.".format("Apple",5.243))
# print("{1:>10.5f}.".format("Apple",5.243))
# print("{1:<10.5f}.".format("Apple",5.243))







# # #20
# n,f,s, = 42,7.03,'String Cheese';
# print("%10.4d. %10.4f. %10.4s"%(n,f,s))
# print("{2} {1} {0}".format(n,f,s))











# # #21
# n,f,s, = 42,7.03,'String Cheese';
# d = {'n':42,'f':7.03,'s':"String Cheese"}
# print("{0[n]} {0[f]} {0[s]}".format(d))
# print("{2:^10s} {1:^10f} {0:^10d}".format(n,f,s))
# print("{0:!^20s}".format("Big Sale"))








# # #22
# z=("kkk",3,3.14,'chn')
# print("{0},{1},{2},{3}".format(*z))








# # #23
print("Product: %(name)5s, Price per unitL %(price)5.5f."%{"name":"Apple", "price":5.243})
print("Product: {name:>5s}, Price per unitL {price:5.5f}.".format(name="Apple", price=5.243))


















