# 4.Write a lambda function which accepts two numbers and returns minimum number.

minimum = lambda a, b: a if a < b else b


def main():
    Ret = minimum(12,11)
    print("Minimum No: ",Ret)

if __name__ == "__main__":
    main()
