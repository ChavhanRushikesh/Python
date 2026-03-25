#Write a program which accepts one number and checks whether it is divisible by 3 and 5.

def Divisible_NO(No):
    if No % 3 == 0:
        if No % 5 == 0:
            print("Divisible By 3 and 5...")
    else:
        print("Number is not Divisible by 3 and 5...")
  
def main():
    Divisible_NO(15)

if __name__ == "__main__":
    main()