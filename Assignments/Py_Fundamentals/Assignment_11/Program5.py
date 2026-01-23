#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which 
#are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from 
#that numbers.(You can also use normal functions instead of lambda functions).

from functools import reduce

#Chk_prime = lambda No : No % 2 != 0


def Chk_prime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

Mult = lambda No : No * 2
Add = lambda A,B : A + B

def main():

    print("Enter number of elements:")
    Size = int(input())

    Data = []
    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Input List =", Data)

    FData = list(filter(Chk_prime, Data))
    if FData :
        print("List after filter =", FData)

        MData = list(map(Mult, FData))
        print("List after map =", MData)

        RData = reduce(Add, MData)
        print("Output of reduce =", RData)

    else:
        print("_" * 80,"\n")
        print("List after filter is empty, Prime numbers are not available..\n")

if __name__ == "__main__":
    main()