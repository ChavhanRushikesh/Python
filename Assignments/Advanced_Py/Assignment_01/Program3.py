#Ass-22
# Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Value1 and Value2.
# Define a constructor (init) that initializes all instance variables to 0.
# Implement the following instance methods:
#  Accept() -accepts values for Valuel and Value2 from the user
#  Addition() - returns the addition of Valuel and Value2.
#  Subtraction() - returns the subtraction of Valuel and Value2.
#  Multiplication() - returns the multiplication of Valuel and Value2.
#  Division ( ) – returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the Value One :"))
        self.Value2 = int(input("Enter the Value two:"))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        if self.Value1 > self.Value2:
            return self.Value1 - self.Value2
        else:
            return self.Value2 - self.Value1
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value1 == 0 or self.Value2 == 0:
            print("Can't Divide by zero ..")
        else:
            return self.Value1 / self.Value2    

def main():
    Obj1 = Arithmetic()
    Obj2 = Arithmetic()

    Obj1.Accept()
    print("Addition      :", Obj1.Addition())
    print("Subtraction   :", Obj1.Subtraction())
    print("Multiplication:", Obj1.Multiplication())
    print("Division      :", Obj1.Division())
    print("-" * 40)

    Obj2.Accept()
    print("Addition      :", Obj2.Addition())
    print("Subtraction   :", Obj2.Subtraction())
    print("Multiplication:", Obj2.Multiplication())
    print("Division      :", Obj2.Division())


if __name__ == "__main__":
    main()