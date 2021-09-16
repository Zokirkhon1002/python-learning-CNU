# score = 20
# print(score)
# score = 30
# print(score)






# width = 10
# height = 20
# area = width * height
# print(area)






# s="Hello, How are you?";
# print(s)
# pi = 3.14592;
# print(pi)






# Let's write a program that prints 
# chicken(1 per person),
# beer(2 cans per person),
# cake(4 per person);

# person = int(input("Enter number of attendees\n>>"))
# chickens = person
# beers = 2 * person
# cakes = 4 * person
# print(f"number of attendees: {person}")
# print(f"number of chickens: {chickens}")
# print(f"number of beer: {beers}")
# print(f"number of cakes: {cakes}")







# exchange values of variables

# x=10
# y=20

# we have to create another variable
# in order to exchange values of variables

# temp = x
# x = y
# y = temp
# print(x)
# print(y)

# another way
# x = y + x
# y = x - y
# x = abs(y-x)
# print(x)
# print(y)






# value = 3
# value = 3.14
# value = "Hello"
# print(value)






# constant 
# TAX_RATE = 0.35
# PI = 3.141592
# MAX_SIZE = 100
# print(TAX_RATE, "\n",MAX_SIZE, "\n",PI)







#  Comments
#  Comments
#  Comments







# this program recieves 2 integers and calculate the Numbers

# x=int(input("First Integer\n>>>"))
# y=int(input("Second Integer\n>>>"))
# sum = x+y
#diff = x - y
# print("The result is: ", sum)
# print("The result is: ", diff)


# a=10
# print(a++)
# SyntaxError: invalid syntax





# print(7/4)
# print(7//4)






# print(2**7)
# a=1000
# r=0.05
# n=10
# print(a*(1+r)**n)





# print(7%4)
# sec = 1000
# min = 1000//60
# remainder = 1000 % 60

# print(min, remainder)









# myMoney = 5000
# priceOfCandy = 120
# numCandies = myMoney//priceOfCandy
# print(numCandies)
# residue = myMoney%priceOfCandy
# print(residue)


# x=2.0
# y=3.0*x**2+7.0*x+9.0
# print(y)
#22-minut





# question 

# startingMoney = 24
# increasing = 1.06
# years = 382
# result = startingMoney * (increasing ** years);
# print(result)








# print(abs(-3))
# print(round(1.9876))
# print(round(1.2345))
# print(min(10, 20, 30, 40, 50))
# print(max(10, 20, 30, 40, 50))






#  importing Module

from math import*

# print(sqrt(4.0))
# x=40
# y=41
# z=sqrt(x+y)
# print(z)






# question 2
# timeFirst = 10/20
# height = sqrt((3**2)+(4**2))
# timeH = height/10
# timeD = height/30
# lastTime = 8/20
# total = timeFirst + timeH + timeD + lastTime
# print(total)





# input() theme

# name = input("Enter your name:\n>>>")
# print(f"Hi, {name}, How are you?")


name = input("What is your name?\n>>>")
gender = input("What is your gender?\n>>>")

if gender == 'male':
    print(f"Nice to meet you Mr {name}")
else:
    print(f"Nice to meet you Ms {name}")

age = input("What is your age?\n>>>")
print(f"oh, your are {age} years old,")

if gender == 'male':
    print(f"Mr {name}")
else:
    print(f"Ms {name}")

