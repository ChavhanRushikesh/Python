#Ass-23
#Write a Python program to implement a class named Numbers with the following
#specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() - returns True if the number is prime, otherwise returns False
# ChkPerfect() - returns True if the number is perfect, otherwise returns False
# Factors() - displays all factors of the number
# SumFactors() - retums the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.

class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are:", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()  

    def SumFactors(self):
        total = 0
        
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        proper_sum = self.SumFactors() - self.Value
        return proper_sum == self.Value


def main():
    Obj1 = Numbers()

    if Obj1.ChkPrime() :
        print("Number is Prime..")
    else:
        print("Not a prime No..")

    Obj1.Factors()
    print("Sum of factors:", Obj1.SumFactors())
    if Obj1.ChkPerfect():
        print("Perfect No..")
    else:
        print("Not a Perfect No..")
    print("-" * 50)
    
    Obj2 = Numbers()
    if Obj2.ChkPrime() :
        print("Number is Prime..")
    else:
        print("Not a prime No..")

    Obj2.Factors()
    print("Sum of factors:", Obj2.SumFactors())
    if Obj2.ChkPerfect():
        print("Perfect No..")
    else:
        print("Not a Perfect No..")

if __name__ == "__main__":
    main()
