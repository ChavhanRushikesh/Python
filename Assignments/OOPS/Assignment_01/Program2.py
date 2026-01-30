#Ass-22
# Write a Python program to implement a class named circle with the following requirements:
# The class should contain three instance variables: Radius, Area, and Circumference.
# The class should contain one class variable named PI, initialized to 3. 14.
# Define a constructor ( init ) that initializes all instance variables to 0.0.
# Implement the following instance methods:
# Accept() - accepts the radius of the circle from the user.
# CalculateArea() - calculates the area of the circle and stores it in the Area variable.
# CalculateCircumference() - caiculates the circumference of the circle and stores it in the Circumference variable.
# Display() - displays the values of Radius, Area, and Circumference.
# Create multiple objects of the Circle class and invoke all the
# iastance methods for each object.

class circle:
   
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
        
    def Accept(self):
        self.radius = float(input("Enter the Radius of circle :"))

    def CalculateArea(self):
        self.area = circle.PI * (self.radius * self.radius)

    def CalculateCircumference(self):
        self.circumference = 2 * circle.PI * self.radius

    def Display(self):
        print("Value of radius        :",self.radius)
        print("Value of area          :",self.area)
        print("Value of Circumference :",self.circumference)

def main():
    obj1 = circle()
    obj2 = circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    print("-" * 40)

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()



if __name__ == "__main__":
    main()