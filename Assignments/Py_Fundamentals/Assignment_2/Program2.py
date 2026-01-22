#Write a program which accepts one number and prints sum of first N natural numbers.

def Sum_No(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + i
    return sum
def main(): 
    Ret = Sum_No(5)
    print("Sum of N natural Numbers :", Ret)

if __name__ == "__main__":
    main()