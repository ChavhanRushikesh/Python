#Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

addition = lambda A, B: A + B

def main():
    data = [11,55,21,7,8,96,3,2]
    print("List of Original Data :",data)

    RData = reduce(addition, data)
    print("Data After reduce :", RData)

if __name__ == "__main__":
    main()