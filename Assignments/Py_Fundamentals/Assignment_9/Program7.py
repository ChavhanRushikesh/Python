#6. Write a program which accept one number and display below pattern.
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


def Patter(No):
    for i in range(1, No + 1):             #Rows
        for j in range(1, No + 1):
            print(j , end=" ")
        print()

def main():
    Patter(5)
        
if __name__ == "__main__":
    main()

