#6. Write a program which accept one number and display below pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

def Patter(No):
    for _ in range(No):            #Rows
        for _ in range(No):          #columns
            print("*",end=' ')
        print() 

def main():
    Patter(5)
        
if __name__ == "__main__":
    main()

