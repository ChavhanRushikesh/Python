#Write a program which accepts one number and prints multiplication table of that number.

def Mul_No(No):
    for i in range(1,11):
        Ans = No * i
        print(Ans)
def main(): 
    Mul_No(4)

if __name__ == "__main__":
    main()