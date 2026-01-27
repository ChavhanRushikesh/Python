# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Thread1(No):
    max_val = No[0]
    for i in No:
        if i > max_val:
            max_val = i
    print("Maximum element :", max_val)

def Thread2(No):
    min_val = No[0]
    for i in No:
        if i < min_val:
            min_val = i
    print("Minimum element :", min_val)

def main():
    data = []

    for i in range(12):
        data.append(int(input(f"Enter number {i+1}: ")))
    print("-" * 40)

    t1 = threading.Thread(target=Thread1, args=(data,))
    t2 = threading.Thread(target=Thread2, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
