#Write a program which accept number from user and return addition of digits in that number.

def Digit_Sum(No):
    sum = 0
    while No != 0:
        rem = No % 10   #Get last digit
        sum = sum + rem #add that
        No = No // 10   #remove last
       
    return sum

def main():
    Ret = Digit_Sum(5187934)
    print("Addition of all Digits :",Ret)
        
if __name__ == "__main__":
    main()
