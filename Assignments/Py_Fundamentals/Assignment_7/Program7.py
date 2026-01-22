#Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

strList= lambda l_String:len(l_String) > 5

def main():
    data = ["Rutvik","Manish","Nikita","Yash","Dhanashree","Raj","Amruta","Shruti"]
    print("List of Original Data :",data)

    FData = list(filter(strList, data))
    print("Data After filter :", FData)

if __name__ == "__main__":
    main()