#Write a program which accepts radius of circle and prints area of circle.
import math

def Circle_Area(red):
    PI = 3.14
    area = PI * red * red
    #area = math.pi * (red * red)
    return area

def main():
    Ret = Circle_Area(5)
    print("Area of Circle : ", Ret)

if __name__ == "__main__":
    main()