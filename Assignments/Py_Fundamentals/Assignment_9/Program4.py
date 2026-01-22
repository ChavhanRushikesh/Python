#Write a program which accept one number form user and return addition of its factors.

def Factors_Add(No):
    sum = 0
    for i in range(1, No):  
        if No % i == 0:
            sum = sum +  i     
    return sum

def main():
    Value = int(input("Enter the No :"))
    Ret = Factors_Add(Value)
    print("Addition of Factors is: ", Ret)
    
if __name__ == "__main__":
    main()

    