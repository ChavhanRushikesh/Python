#Write a program which accepts one number and prints square of that number.

def SquareNo(No):
    Ans = No * No
    return Ans
def main():
    Ret = SquareNo(5)
    print("Square Of No:",Ret)

if __name__ == "__main__":
    main()