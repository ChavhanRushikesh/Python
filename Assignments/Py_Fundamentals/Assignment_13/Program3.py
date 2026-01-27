# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading

# Shared counter means global variable
counter = 0
lock = threading.Lock()  

def Thread1(No):
    global counter
    for _ in range(No):
        with lock:         
            counter = counter + 1


def Thread2(No):
    global counter
    for _ in range(No):
        with lock:         
            counter = counter + 1


def Thread3(No):
    global counter
    for _ in range(No):
        with lock:         
            counter = counter + 1


def Thread4(No):
    global counter
    for _ in range(No):
        with lock:         
            counter = counter + 1


def main():
    global counter

    t1 = threading.Thread(target=Thread1, args=(1000,))
    t2 = threading.Thread(target=Thread2, args=(1000,))
    t3 = threading.Thread(target=Thread3, args=(1000,))
    t4 = threading.Thread(target=Thread4, args=(1000,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()
