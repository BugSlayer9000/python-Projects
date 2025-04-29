from bankapp import *

Dave = bankaccount(1000,"Dave")
Sara = bankaccount(1500,"Sara")

Dave.getBalance()

Sara.Deposit(200)

Dave.Withdraw(200)

Sara.Transfer(10000, Dave)



