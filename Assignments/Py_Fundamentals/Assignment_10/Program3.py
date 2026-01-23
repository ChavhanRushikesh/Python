#Write a program which accept N Numbers of list from user and store it into list. Return minimum number from that list.

def Minimum(Arr):
    min = Arr[0]
    for i in range(len(Arr)):
        if Arr[i] < min:
            min = Arr[i]
    return min

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

    Ret = Minimum(Data)
    print("Minimum is : ", Ret)

if __name__ == "__main__":
    main()
