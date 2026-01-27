# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.


import threading

lock = threading.Lock()

def Check_Prime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Prime(num):
    with lock:
        prime_num = []
        for i in num:
            if Check_Prime(i):
                prime_num.append(i)
    
        print("Prime numbers:", prime_num)
        print("-" * 80)

def NonPrime(num):
    with lock:
        prime_No = []
        for i in num:
            if Check_Prime(i) == False:
                prime_No.append(i)
    
        print("Non Prime numbers:", prime_No)

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
