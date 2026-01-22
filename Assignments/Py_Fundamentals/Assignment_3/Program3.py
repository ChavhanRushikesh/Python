#Write a program which accepts one number and prints sum of digits.

def Digit_Sum(No):
    sum = 0
    while No > 0:
        rem = No % 10
        sum = sum + rem
        No = No // 10
    return sum
   
def main(): 
   Ret = Digit_Sum(2001)
   print("SUm of Digits :", Ret)
 
if __name__ == "__main__":
    main()