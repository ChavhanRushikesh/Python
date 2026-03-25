#Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

divisible = lambda No: No % 3 == 0 and No % 5 == 0

def main():
    data = [15,55,30,7,45,96,3,60]
    print("List of Original Data :",data)

    FData = list(filter(divisible, data))
    print("Data After filter :", FData)

if __name__ == "__main__":
    main()