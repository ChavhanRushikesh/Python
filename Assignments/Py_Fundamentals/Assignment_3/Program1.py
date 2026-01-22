#Write a program which accepts one number and checks whether it is prime or not.

def Prime_No(No):
    if No >= 2:
        return True
    for i in range(2,No + 1):
        if No % i == 0:
            return False
        else:
            return True
        
def main(): 
    Ret = Prime_No(11)
    if Ret == True:
        print("Prime Number..")
    else:
        print("Not a Prime Number..")
 
if __name__ == "__main__":
    main()