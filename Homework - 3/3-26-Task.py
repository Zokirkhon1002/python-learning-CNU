"""
Created on Fri Oct 15 02:53:17 2021

Student number: 180421
Full Name: KOTIBKHONOV ZOKIRKHON ZOKHIDKHON UGLI

"""

#Task:
# Write the result of the program.

colors=['white','silver']
cars=['granzur', 'avante']
colored_cars=[(x,y) for x in colors for y in cars]
print(colored_cars)

# Output
# [('white', 'granzur'), ('white', 'avante'), ('silver', 'granzur'), ('silver', 'avante')]
