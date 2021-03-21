#Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class Account:
    def __init__(self):
        self.balance=0
        self.accountnumber=int(input("Enter your Account number : "))
        self.name=input("Enter your name : ")
        self.accounttype=input("Enter your Account type : ")
    def display(self):
        print("Name : ",self.name)
        print("Account number : ",self.accountnumber)
        print("Account type : ",self.accounttype)
    def deposit(self):
        amount=int(input("Enter the amount to be deposited:"))
        self.balance+=amount
        print("your account balance is:",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount to be withdrawn:"))
        if(amount>self.balance):
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
            print("your account balance is : ",self.balance)
account=Account()
account.display()
account.deposit()
account.withdraw()

