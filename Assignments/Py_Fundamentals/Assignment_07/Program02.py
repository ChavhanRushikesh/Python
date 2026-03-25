#Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

even = lambda No: No % 2 == 0

def main():
    data = [11,55,21,7,8,96,3,2]
    print("List of Original Data :",data)

    FData = list(filter(even, data))
    print("Data After filter :", FData)

if __name__ == "__main__":
    main()