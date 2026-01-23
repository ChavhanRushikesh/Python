# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List.Main python file 
# accepts N numbers from user a each number to ChkPrime() function which is part of our user defined module name MarvellousNum. Name of the
# function from main python file should be ListPrime().

import MarvellousNum

def ListPrime(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if MarvellousNum.ChkPrime(Arr[i]):
            Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the Number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the Elements:")

    for _ in range(Size):
        Value = int(input())
        Data.append(Value)     #Data[i] = value

    print(Data)

    Ret = ListPrime(Data)
    print("Addition of prime numbers is:", Ret)

if __name__ == "__main__":
    main()
