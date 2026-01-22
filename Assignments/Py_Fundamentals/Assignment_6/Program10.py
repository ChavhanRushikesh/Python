# Write a lambda function which accepts three numbers and returns largest number.

largest_No = lambda a, b, c: a if a > b and a > c else (b if b > c else c)

def main():
    Ret = largest_No(59,16,55)
    print("largest No is :", Ret)

if __name__ == "__main__":
    main()