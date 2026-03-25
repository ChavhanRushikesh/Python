# Write a lambda function which accepts two numbers and returns maximum number.
maximum = lambda a, b: a if a > b else b

def main():
    Ret = maximum(9,11)
    print("Maximum No: ",Ret)
    # if Ret == True:
    #     print("Maximum No: ",Ret)
    # else:
    #     print("Maximum No: ",Ret)

if __name__ == "__main__":
    main()
