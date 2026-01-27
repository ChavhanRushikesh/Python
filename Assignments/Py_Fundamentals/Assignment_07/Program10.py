#Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

even_Count = lambda No: No % 2 == 0

def main():
    data = [15,55,30,7,45,96,3,60]
    print("List of Original Data :",data)

    FData = list(filter(even_Count, data))
    print("Data After filter :", len(FData))

if __name__ == "__main__":
    main()