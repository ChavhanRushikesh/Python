#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements. 

from functools import reduce

product_No = lambda A, B: A * B

def main():
    data = [15,55,30,7,45,96,3,60]
    print("List of Original Data :",data)

    RData = reduce(product_No, data)
    print("Data After filter :", RData)

if __name__ == "__main__":
    main()