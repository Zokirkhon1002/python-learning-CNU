def makeCall():
    print("Calling...")

makeCall();
print(f"phone.py's module name is {__name__}")

if __name__ == "__main__":
    print("phone.py is being run directly")