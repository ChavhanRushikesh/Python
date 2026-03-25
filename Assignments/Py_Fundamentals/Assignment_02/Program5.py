#Write a program which accepts one number and prints all Odd numbers till that number.

def Odd_No(No):
    for i in range(1,No+1):
        if i % 2 == 1:
            print("Odd Numbers :", i)
def main(): 
    Odd_No(10)
 
if __name__ == "__main__":
    main()