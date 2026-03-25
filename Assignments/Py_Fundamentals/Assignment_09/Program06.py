#6. Write a program which accept one number and display below pattern.
# * * * * *
# * * * *
# * * *
# * *
# *


def Patter(No):
    for i in range(No):             #Rows
        for _ in range(No - i):
            print("*", end=" ")
        print()

    # for i in range(No, 0, -1):
    #     print("* " * i)

def main():
    Patter(5)
        
if __name__ == "__main__":
    main()

