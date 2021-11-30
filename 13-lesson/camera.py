def photo():
    print("Taking a photo...")

photo()
print(f"camera.py's module name is {__name__}")

if __name__ == "__main__":
    print("phone.py is being run directly")