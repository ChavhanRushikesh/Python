#Write a program which accepts one number and prints cube of that number.

def CubeNo(No):
    Ans = No * No * No
    return Ans
def main():
    Ret = CubeNo(4)
    print("Cube Of No:",Ret)

if __name__ == "__main__":
    main()