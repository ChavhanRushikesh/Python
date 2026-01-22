#Write a program which accepts one number and prints reverse of that number.

def Rev_No(No):
    rev = 0
    while No > 0:
        rev = (rev * 10) + No % 10 
        No = No // 10

        # rem = No % 10
        # rev = rev * 10 + rem
        # No = No // 10
    return rev  
   
def main(): 
   Ret = Rev_No(2001)
   print("Reverse No :", Ret)
 
if __name__ == "__main__":
    main()