#write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which 
#are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will
#increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce

Chk_No = lambda No : No >= 70 and No <= 90
Add = lambda No : No + 10
Product = lambda A,B : A * B

def main():

    print("Enter number of elements:")
    Size = int(input())

    Data = []
    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Input List =", Data)

    FData = list(filter(Chk_No, Data))
    if FData :
        print("List after filter =", FData)

        MData = list(map(Add, FData))
        print("List after map =", MData)

        RData = reduce(Product, MData)
        print("Output of reduce =", RData)

    else:
        print("_" * 80,"\n")
        print("List after filter is empty, numbers are not available between 70 to 90..\n")

if __name__ == "__main__":
    main()