###1
## university
# s = input("Enter a word: ")
# vowels = "aeiouAEIOU"
# result = ""
# for letter in s:
#     if letter not in vowels:
#         result += letter

# print(result) #output: nvrsty




###2
# def sub():
#     global s
#     print(s)
#     s = "Banana is good"
#     print(s)

# s = "Apple is good"
# sub()
# print(s)



##3
# rows = 3
# cols = 2
# table = []
# for row in range(rows):
#     table += [[1]*cols]
# print(table)

# for row in range(rows):
#     for col in range(cols):
#         table[row][col] = (row + col)
# print(table)



###4
# print(5 and 7)
# print(0 or 5)



###5
# L=[lambda x:x**2, lambda x:x**3, lambda x:x**4,]
# for f in L:
#     print(f(3))



###6
# import sys
# if __name__ == '__main__':
#     print(f"Number of argv: {len(sys.argv)}")
#     for item in sys.argv:
#         print(item)




####
# dict1 = {x:x*x*x for x in range(5)}
# print(dict1)




# n = int(input("enter an integer: "))
# sum = 0
# temp = 0
# while n>0:
#     temp += 1;
#     sum += temp
#     n-=1
# print(sum)













""" 
    Write a function that checks if a given string (case insensitive) is a palindrome.

    A palindrome is a word, number, phrase, or other sequence of characters 
    which reads the same backward as forward, such as madam or racecar.
"""

## print(is_palindrome('a')) # True
## print(is_palindrome('aba')) # True
## print(is_palindrome('Abba')) # True
## print(is_palindrome('malam')) # True
## print(is_palindrome('walter')) # False
## print(is_palindrome('kodok')) # True
## print(is_palindrome('Kasue')) # False





### my solution
def is_palindrome(s):
    s = s.lower()
    listfor = []
    for i in s:
        listfor.append(i)
    listfor.reverse()
    result = "".join(listfor)
    return s == result






### another solution
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]


print(is_palindrome('a')) # True
print(is_palindrome('aba')) # True
print(is_palindrome('Abba')) # True
print(is_palindrome('malam')) # True
print(is_palindrome('walter')) # False
print(is_palindrome('kodok')) # True
print(is_palindrome('Kasue')) # False








