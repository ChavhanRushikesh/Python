#Write a program which accept N Numbers of list from user and store it into list. Return maximum number from that list.

def Maximum(Arr):
    max = Arr[0]
    for i in range(len(Arr)):
        if Arr[i] > max:
            max = Arr[i]
    return max

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the Number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the Elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     #Data[i] = value

    print(Data)

    Ret = Maximum(Data)
    print("Maximum is : ", Ret)

if __name__ == "__main__":
    main()
