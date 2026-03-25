#Write a program which accept number from user and print that number of "*" on screen.

def Num(No):
   for _ in range(No):
      print(" * ",end='')

def main():
   Value = int(input("Enter the Number :"))
   Num(Value)
    
if __name__ == "__main__":
    main()