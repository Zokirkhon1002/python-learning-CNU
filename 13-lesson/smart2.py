from smart import *
print("-"*10)
while True:
    choice = input("What do you want?: ")
    if choice == '0':
        break
    if choice == '1':
        camera.photo()
    elif choice == '2':
        phone.makeCall()
    elif choice == '3':
        print("Function implemented later")
print("Program ended")