#Write a program which accept one number and display below pattern.(rows 5, columns 5)

def Pattern(No):
    for _ in range(No):            #Rows
        for _ in range(No):          #columns
            print("*",end=' ')
        print()

def main():
    Pattern(5)
    
if __name__ == "__main__":
    main()

    