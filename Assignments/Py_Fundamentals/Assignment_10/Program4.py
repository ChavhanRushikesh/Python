#Write a program which accept N Numbers of list from user and store it into list. 
# Accept one another number from user and return frequency of that number from List,

def Frequency(Arr, No):
    count = 0

    for i in range(len(Arr)):
        if Arr[i] == No:
            count = count + 1

    return count

def main():
    Size = 0
    Value = 0
    Ret = 0
    No = 0

    print("Enter the Number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the Elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     #Data[i] = value

    print(Data)

    print("Enter the number to check frequency:")
    No = int(input())

    Ret = Frequency(Data, No)
    print("Frequency of", No, "is:", Ret)

if __name__ == "__main__":
    main()
