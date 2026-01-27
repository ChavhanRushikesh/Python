#Write a program which accepts one number and prints binary equivalent.

def binary_Equivalent(No):
    if No == 0:
        print("Binary equivalent: 0")
    else:
        binary = ""
        while No > 0:
            binary = str(No % 2) + binary
            No //= 2
        print("Binary equivalent:", binary)

def main():
    binary_Equivalent(6)
   
if __name__ == "__main__":
    main()