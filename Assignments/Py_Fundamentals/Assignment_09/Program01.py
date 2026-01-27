#Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for for multiplication
#and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all 
#the functions from Arithmetic module by accepting the parameters from user.

import Arithmatic

def main():
    print("Addition of two Numbers :",Arithmatic.Add(12,25))
    print("Addition of two Numbers :",Arithmatic.Sub(25,65))
    print("Addition of two Numbers :",Arithmatic.Mult(12,25))
    print("Addition of two Numbers :",Arithmatic.Div(5,25))

if __name__ == "__main__":
    main()