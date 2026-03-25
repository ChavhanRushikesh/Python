#Write a program which contains filter(), map() and reduce() in it. Python application which contains as one list of numbers. List contains the numbers 
#which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return 
#addition of all that numbers.

from functools import reduce

Chk_even = lambda No : No % 2 == 0
Square = lambda No : No * No
Add = lambda A,B : A + B

def main():

    print("Enter number of elements:")
    Size = int(input())

    Data = []
    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Input List =", Data)

    FData = list(filter(Chk_even, Data))
    if FData :
        print("List after filter =", FData)

        MData = list(map(Square, FData))
        print("List after map =", MData)

        RData = reduce(Add, MData)
        print("Output of reduce =", RData)

    else:
        print("_" * 80,"\n")
        print("List after filter is empty, Even numbers are not available..\n")

if __name__ == "__main__":
    main()