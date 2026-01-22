#Write a program which accepts one number and prints its factors.

def factors_No(No):

    for i in range(1, No + 1):
        if No % i == 0:
            print("Factors of No :",i)

def main(): 
    factors_No(12)
 
if __name__ == "__main__":
    main()


# import threading

# factors_list = []

# def factors_No(No):
#     global factors_list

#     for i in range(1, No + 1):
#         if No % i == 0:
#             factors_list.append(i)

# def main(): 
#     No = 12
#     t1 = threading.Thread(target=factors_No, args=(No,))
#     t1.start()
#     t1.join()

#     print("Factors of No : ", factors_list)
 
# if __name__ == "__main__":
#     main()

    
