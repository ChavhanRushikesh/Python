#Write a program which accepts one number and checks whether it is palindrome or not.

def palindrome_No(No):
    Default_No = No
    rev = 0

    while No > 0:
        rev = (rev * 10) + No % 10 
        No = No // 10

    if Default_No == rev:
        return True
    else:
        return False
   
def main(): 
   Ret = palindrome_No(121)
   if Ret == True:
      print("palindrome No..")
   else:
      print("Not a palindrome No..")
 
if __name__ == "__main__":
    main()