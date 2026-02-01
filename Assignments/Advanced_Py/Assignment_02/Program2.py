#Ass-23
# Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (init) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display () - displays account holder name and current balance
# Deposit () - accepts an amount from the user and adds it to balance
# Withdraw () - accepts an amount from the user and subtracts it from balance 
# (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest() - calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
 
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.name = Name
        self.amount = Amount

    def Display(self):
        print("Account Holder Name:", self.name)
        print("Current Balance:", self.amount)

    def Deposit(self):
        deposit_amt = float(input("Enter amount to deposit : "))
        self.amount = self.amount + deposit_amt
        print("Amount deposited successfully..!!")

    def Withdraw(self):
        withdraw_amt = float(input("Enter amount to withdraw : "))

        if withdraw_amt > self.amount:
            print("Insufficient balance!! Withdrawal failed.")
        else:
            self.amount = self.amount - withdraw_amt
            print("Amount withdrawn successfully..!!")

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        return interest

def main():
   
    Obj1 = BankAccount("Ramalal Chunalal Patel", 50000)
    Obj2 = BankAccount("Bhilaji Rambhau Shinde", 10000)

    print("_" * 50)
    Obj1.Display()
    print("-" * 50)
    Obj1.Deposit()
    Obj1.Withdraw()
    print("Interest on current balance:", Obj1.CalculateInterest())
    Obj1.Display()
    print("_" * 50)

  
    print("_" * 50)
    Obj2.Display()
    print("-" * 50)
    Obj2.Deposit()
    Obj2.Withdraw()
    print("Interest on current balance:", Obj2.CalculateInterest())
    Obj2.Display()
    print("_" * 50)


if __name__ == "__main__":
    main()
