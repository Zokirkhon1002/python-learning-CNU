# command_arguments" ca.py
print("Test program")
import sys

if __name__ == "__main__":
    print(f"Number of argv: {len(sys.argv)}")
    for arg in sys.argv:
        print(arg)