#Write program which accept one number for user and check whether number is prime or not.

def Check_No(No):
    for i in range(No + 1):
        if No == 2:
            return True
        
        if No % 2 == 0:
            return False
        
        else:
            return True

def main():
    Ret = Check_No(5)
    if Ret:
        print("Number is Prime..")  
    else:
        print("Number is Not Prime..")
        
if __name__ == "__main__":
    main()

    