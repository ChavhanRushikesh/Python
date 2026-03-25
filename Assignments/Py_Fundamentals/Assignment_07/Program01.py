#Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

square = lambda No: No * No

def main():
    data = [11,55,21,7,8,96,3,2]
    print("List of Original Data :",data)

    MData = list(map(square, data))
    print("Data After Map :", MData)

if __name__ == "__main__":
    main()