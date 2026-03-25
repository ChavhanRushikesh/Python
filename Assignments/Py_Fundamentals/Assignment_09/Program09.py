#Write a program which accept number from user and return number of digits in that number.

def Digit_Count(No):
    Count = 0
    while No > 0:
        No = No // 10
        Count = Count + 1
    return Count

def main():
    Ret = Digit_Count(5187934)
    print("Count of all Digits :",Ret)
        
if __name__ == "__main__":
    main()
