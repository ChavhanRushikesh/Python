#Write a program which accepts length and width of rectangle and prints area..

def Rectangle(len, wid):
    area = len * wid
    return area
def main():
    Ret = Rectangle(4,4)
    print("Area of Rectangle : ", Ret)

if __name__ == "__main__":
    main()