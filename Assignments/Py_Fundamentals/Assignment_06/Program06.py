# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

odd = lambda x: x % 2 != 0

def main():
    Ret = odd(12)

    if Ret == True:
        print(Ret)
    else:
        print(Ret)

if __name__ == "__main__":
    main()