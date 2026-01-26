# Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization

import threading

lock = threading.Lock()

def Thread1(No):
    with lock: 
        numbers = []
        for i in range(1,No + 1):   
            numbers.append(i)
            
        print("Numbers From 1 to 50 :",numbers)
        print("-" * 120)
        
def Thread2(No):
    with lock:
        numbers = []
        for i in range(No,0,-1):  
            numbers.append(i)
    
        print("Numbers From  50 to 1 :",numbers)
        
def main():

    t1 = threading.Thread(target=Thread1,args=(50,))
    t2 = threading.Thread(target=Thread2, args=(50,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()