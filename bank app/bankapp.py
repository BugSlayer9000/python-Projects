# samod subhasha
# 17/04/25
# this is bank app using OOP in python

class BalanceExeption(Exception):
    pass
    
class bankaccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.Name = acctName
        print(
            f"\nAccount '{self.Name} Created. \nbalance = £{self.balance:.2f}'"
        )
    
    def getBalance(self):
        print(
            f"\nAccount '{self.Name}' balance  £{self.balance:.2f}'"
        )
    
    def Deposit(self, amount):
        self.balance += amount
        print("\nDeposit Complete.")
        self.getBalance()
    
    def ViableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceExeption(
                f"\nSorry, Account '{self.Name}' Only has a balance of £{self.balance:.2f}"
            )
        
    def Withdraw(self, amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete!")
        except BalanceExeption  as error:
            print(f"\nWithdraw Inturrupted: {error}")
    
    def Transfer(self, amount, account):
        try:
            print("\n*****************\n\nBegining Transfer..")
            self.ViableTransaction(amount)
            account.Deposit(amount)
            print("\nTransfer complete...\n*****************")
        except BalanceExeption as error:
            print(f"\nTransfer Inturupted!{error}")

class InterestReward(bankaccount):
    def Deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


        
    