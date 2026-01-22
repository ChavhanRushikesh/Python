#Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

minELement = lambda A, B: A if A < B else B

def main():
    data = [11,55,21,7,8,96,3,2]
    print("List of Original Data :",data)

    RData = reduce(minELement, data)
    print("Data After reduce :", RData)

if __name__ == "__main__":
    main()