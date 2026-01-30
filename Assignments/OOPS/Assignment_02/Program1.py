#Ass-23
# Write a Python program to implement a class named Bookstore with the following specifications:
# The class should contain two instance variables:
# Name (Book Name)
# Author (Book Author)
# The class should contain one class variable:
# No Of Books (initialize it to 0)
# Define a constructor (init) that accepts Name and Author and initializes instance variables.
# Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is
# created.
# Implement an instance method:
# Display() - should display book details in the format: <BookName> by <Author>. No of books: <No0fBooks>
# Example usage:
# Obj1 = BookStore("Linux System em Programming", "Robert Love") Objl.Display() # Linux System Programming by Robert Love. No of
# books: 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie") Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2

class Bookstore:
    NoOfBooks = 0
    
    def __init__(self,Name,Author):
        self.name = Name
        self.author = Author
        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1

    def Display(self):
        print(f"{self.name} by {self.author} No Of Books : {Bookstore.NoOfBooks}")

def main():
    print("-" * 60)

    Obj1 = Bookstore("Linux System Programming","Robart Love")
    Obj1.Display()
    print("-" * 60)

    Obj2 = Bookstore("C Programming","Dennis Ritchie")
    Obj2.Display()
    print("-" * 60)

    Obj3 = Bookstore("Java Programming","Herbert Schildt")
    Obj3.Display()
    print("-" * 60)

    Obj4 = Bookstore("Python Programming","John Zelle")
    Obj4.Display()
    print("-" * 60)

if __name__ == "__main__":
    main()