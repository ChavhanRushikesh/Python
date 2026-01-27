# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading
lock = threading.Lock()
def Thread1(No):
    Sum = 0
    for i in No:
        Sum += i 
    return Sum
    
def Thread2(No):
    product = 1
    for i in No:
        product *= i 
    return product

def main():
    data = [1,2,3,4,5,6,7,8,9,10,11,12]
    Ret1 = Thread1(data)
    Ret2 = Thread2(data)

    t1 = threading.Thread(target=Thread1, args=(data,))
    t2 = threading.Thread(target=Thread2, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    with lock:
        print("Sum of total elements : ",Ret1)
    print("Product of elements   :",Ret2)

if __name__ == "__main__":
    main()

