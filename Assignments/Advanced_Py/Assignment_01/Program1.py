#Ass-22
# Write a Python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables: nol and no2.
# The class should contain one class variable named Value
# a constructor (init) that accepts two parameters and initializes the instance variables.
# Implement two instance methods:
# Fun () - displays the values of instance variables no1 and no2.
# Gun () - displays the values of instance variables no1 and no2
# Create two objects of the Demo class as follows:
# Objl = Demo (11, 21)
# Obj2 = Demo (51, 101)
# Call the instance methods in the given sequen
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
   
    Value = None

    def __init__(self,num1,num2):
        self.no1 = num1
        self.no2 = num2
        

    def Fun(self):
        print("Fun method called..")
        print("Value of No1 :",self.no1)
        print("Value of No2 :",self.no2)
        print("-" * 80)

    def Gun(self):
        print("Gun method called..")
        print("Value of No1 :",self.no1)
        print("Value of No2 :",self.no2)
        print("-" * 80)

def main():
    Obj1 = Demo (11, 21)
    Obj2 = Demo (51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()