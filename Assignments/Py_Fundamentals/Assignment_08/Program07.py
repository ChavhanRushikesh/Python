# Write a program which contains one function that accept one number form user and returns true if number is divisible by 5 otherwise return false.

def Check_No(No):
   return No % 5 == 0

def main():
   Value = int(input("Enter the Number :"))
   Ret = Check_No(Value)
   print(Ret)
    
if __name__ == "__main__":
    main()