#Write a lambda function which accepts one number and returns True if number is even otherwise False.

even = lambda x: x % 2 == 0


def main():
    Ret = even(12)
    if Ret == True:
        print("Even No: ",Ret)
    else:
        print(Ret)

if __name__ == "__main__":
    main()