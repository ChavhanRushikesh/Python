# Write a program which accept number from user and check whether that number is positive negative or zero

def Check_No(No):
    if No >= 0:
        print("Number is Positive..")
    elif No < 0:
        print("Number is Negetive..")
    else:
        print("Number is Zero..")

def main():
   Value = int(input("Enter the Number :"))
   Check_No(Value)
    
if __name__ == "__main__":
    main()