#Write a program which accepts one number and checks whether it is perfect number or not.

def checks_perfect(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
    if sum == No:
        return True

def main():
    Ret = checks_perfect(6)
    if Ret == True:
        print("Perfect No..")
    else:
        print("Not Perfect No..")

if __name__ == "__main__":
    main()