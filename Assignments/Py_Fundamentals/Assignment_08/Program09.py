#Write a program which display first 10 even numbers on screen.

def Num(No):
   for i in range(2,No + 1,2):
      print(i, end=' ')

def main():
   Num(20)
 
if __name__ == "__main__":
    main()