#Write a program which accepts marks and displays grade..

def Marks(per):
    if per >= 75:
        print("Distinction..")
    elif per >= 60:
        print("First Class..")
    elif per >= 50:
        print("Second Class..")
    elif per >= 40:
        print("pass..")
    else:
       print("Fail..")

def main():
    Marks(90.91)

if __name__ == "__main__":
    main()