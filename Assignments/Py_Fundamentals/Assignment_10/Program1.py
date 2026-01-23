#Write a program which accept N Numbers of list from user and store it into list. Return addition of all elements from that list.
def Summetion(Arr):
    sum = 0

    for i in range(len(Arr)):
        sum = sum + Arr[i]
    return sum

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

    Ret = Summetion(Data)
    print("Summetion is : ", Ret)

if __name__ == "__main__":
    main()