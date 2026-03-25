#Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

lock = threading.Lock()

def Even():
    with lock: 
        print("Even Numbers :")
        for i in range(2,21,2):
            print(i, end=' ')
    
def Odd():
    with lock:
        print("\nOdd Numbers :")
        for i in range(1,20,2):
            print(i, end=' ')
        
def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()