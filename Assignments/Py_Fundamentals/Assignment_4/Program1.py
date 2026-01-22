#Write a program which accepts one character and checks whether it is vowel or consonant.

def Check_Vowel(vowel):
    if vowel == 'a' or 'e' or 'i' or 'o' or 'u':
        return True
    else:
        return False
    
def main(): 
    Ret = Check_Vowel('a')
    if Ret == True:
        print("vowel..")
    else:
        print("consonant..")
 
if __name__ == "__main__":
    main()