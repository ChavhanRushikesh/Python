# Write a lambda function which accepts one number and returns True if divisible by 5.

divisible = lambda x: x % 5 == 0


def main():
    Ret = divisible(12)

    if Ret == True:
        print(Ret)
    else:
        print(Ret)

if __name__ == "__main__":
    main()