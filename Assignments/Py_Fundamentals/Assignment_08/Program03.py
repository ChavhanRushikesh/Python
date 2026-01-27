#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(No1, No2):
    return No1 + No2

def main():
    value1 = int(input("Enter the Number first :"))
    value2 = int(input("Enter the Number first :"))

    Ret = Add(value1, value2)
    print("Addition is :",Ret)
    
    
if __name__ == "__main__":
    main()