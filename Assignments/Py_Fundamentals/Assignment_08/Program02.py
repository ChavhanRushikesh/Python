#Write a program which contains one function named as ChkNum() which accept one parameter as r as number. 
#If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(No):
    return No % 2 == 0

def main():
    Ret = ChkNum(11)
    if Ret :
        print("No is Even..")
    else:
        print("No is Odd..")
    
if __name__ == "__main__":
    main()