#Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
#   . Extract all even elements from the
#   . Calculate and display their sum.
# The OddList thread should:
#   . Extract all odd elements from the list.
#   . Calculate and display their sum.
# Threads should run concurrently.

import threading

lock = threading.Lock()

def EvenList(No):
    with lock: 
        sum = 0
        even_ele = []
        for i in No:    #for each loop
            if i % 2 == 0:
                even_ele.append(i)
                sum = sum + i
        print("List of Even Elements :",even_ele)
        print("Sum of Even elements :",sum)
        print("-" * 55)
        
def OddList(No):
    with lock:
        sum = 0
        odd_ele = []
        for i in No:
            if i % 2 == 1:
                odd_ele.append(i)
                sum = sum + i
        print("List Of Odd Elements :",odd_ele)
        print("Sum of Odd ELements :",sum)
        
def main():
    data = [10,15,42,58,75,845,25,27,56,98,87,25]

    t1 = threading.Thread(target=EvenList,args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()