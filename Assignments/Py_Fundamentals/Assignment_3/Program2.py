#Write a program which accepts one number and prints count of digits in that number.

def Digit_Count(No):
    count = 0
    while No > 0:
        count = count + 1
        No = No // 10
    return count
   
def main(): 
   Ret = Digit_Count(213115)
   print("Digits of No :",Ret)
 
if __name__ == "__main__":
    main()