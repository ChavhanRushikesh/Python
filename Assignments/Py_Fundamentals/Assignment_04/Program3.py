#Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Calculator(No1, No2):
    def add():
        return No1 + No2
    def sub():
        if No1 > No2:
            return No1 - No2
        else:
            return No2 - No1
    def mul():
        return No1 * No2
    def div():
        return No1 / No2

    return add,sub,mul,div

def main():
    
    add_f, sub_f, mul_f, div_f = Calculator(11, 25)
    
    print("Addition is :", add_f())
    print("Subtraction is :", sub_f())
    print("Multiplication is :", mul_f())
    print("Division is :", div_f())

if __name__ == "__main__":
    main()