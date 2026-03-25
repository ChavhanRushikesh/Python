# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

lock = threading.Lock()

def Small(String):
    with lock: 
        count = 0
        lowercase_chars = []
        
        for ch in String:
            if 'a' <= ch <= 'z':    
                lowercase_chars.append(ch)
                count = count + 1
                
        print("Count of Lowercase Charecters :",count)
        print("Lowercase Charecters :",lowercase_chars)
        
def Capital(String):
    with lock:
        count = 0
        uppercase_chars = []
        
        for ch in String:
            if 'A' <= ch <= 'Z':    
                uppercase_chars.append(ch)
                count = count + 1
                
        print("Count of uppercase Charecters :",count)
        print("uppercase Charecters :",uppercase_chars)

def Digits(String):
    with lock:
        count = 0
        digits = []
        
        for ch in String:
            if '0' <= ch <= '9':    
                digits.append(ch)
                count = count + 1
                
        print("Count of Digits from string :",count)
        print("Digits in string :",digits)
        
def main():
    data ="1. Hooking Hooking is a technique used to intercept or modify the behavior of a program, function, or system call 2. Hacking Hacking is a broader term that usually refers to unauthorized access or manipulation of a computer system, network, or program"
 
    t1 = threading.Thread(target=Small,args=(data,))
    t2 = threading.Thread(target=Capital, args=(data,))
    t3 = threading.Thread(target=Digits,args=(data,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()