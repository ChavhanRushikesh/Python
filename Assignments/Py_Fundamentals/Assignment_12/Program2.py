#Design a Python application that creates two threads named EvenFactor and OddFactor.
#. Both threads should accept one integer number as a parameter.
#. The EvenFactor thread should:
#   . Identify all even factors of the given number.
#   . Calculate and display the sum of even factors.
# . The OddFactor thread should:
#   . Identify all odd factors of the given number.
#   . Calculate and display the sum of odd factors.
# . After both threads complete execution, the main thread should display the message: "Exit from main"

import threading

lock = threading.Lock()

def EvenFactor(No):
    with lock: 
        sum = 0
        even_fact = []
        for i in range(1, No + 1):
            if No % i == 0 and i % 2 == 0:
                even_fact.append(i)
                sum = sum + i
        print("Even Factors are :",even_fact)
        print("Sum of Even Factors :",sum)
    
def OddFactor(No):
    with lock:
        sum = 0
        odd_fact = []
        for i in range(1,No + 1):
            if No % i == 0 and i % 2 == 1:
                odd_fact.append(i)
                sum = sum + i
        print("Odd Factors are :",odd_fact)
        print("Sum of Odd Factors :",sum)
        
def main():
    t1 = threading.Thread(target=EvenFactor,args=(12,))
    t2 = threading.Thread(target=OddFactor,args=(12,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()