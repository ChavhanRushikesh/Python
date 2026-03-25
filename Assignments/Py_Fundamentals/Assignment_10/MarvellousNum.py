# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List.Main python file 
# accepts N numbers from user a each number to ChkPrime() function which is part of our user defined module name MarvellousNum. Name of the
# function from main python file should be ListPrime().
#Ass-10/Program5

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True
