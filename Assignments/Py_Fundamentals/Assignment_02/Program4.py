#Write a program which accepts one number and prints all even numbers till that number.

def Even_No(No):
    for i in range(1,No+1):
        if i % 2 == 0:
            print("Even Numbers :", i)
def main(): 
    Even_No(10)
 
if __name__ == "__main__":
    main()