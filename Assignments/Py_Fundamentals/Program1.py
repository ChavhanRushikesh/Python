#use of all functions in Python

import sys

task = "Jay Ganesh"
task1 = {10,20,30,40}
task2 = {"Name" : "Rahul" , "Age" : 20}

print(id(task))                     #print Address

print(type(task))                   #print type Str

print(len(task))                    #print length of 10

print(isinstance(task,str))         #print boolean value and show the istance is str or not

print(sys.getsizeof(task))          #print size in byte

print(dir(task))                    #Display the list of attributes and methods

print(help(task))                   #print Documentation for the object that we can provide
print(help(str))

print(hash(task))                   #print hash value a random number
print(hash(task2))                  #print Error
print(hash(task1))                  #print a Error 