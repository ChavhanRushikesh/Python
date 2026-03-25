#Write a program which accept one number from user and return its factorial.

def Fact_No(No):
    fact = 1
    for i in range(1, No + 1):  
        fact = fact *  i     
    return fact

def main():
    Value = int(input("Enter the No :"))
    Ret = Fact_No(Value)
    print("Factorial of no ",Value ,"is :", Ret)
    
if __name__ == "__main__":
    main()

    