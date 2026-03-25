#Write a program which accepts one number and prints factorial of that number.

def Fact_No(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact
def main(): 
    Ret = Fact_No(5)
    print("Factorial of Numbers :", Ret)

if __name__ == "__main__":
    main()