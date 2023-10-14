class BankAccount:

    def __init__(self,accountNumber,balance):
        self._accountNumber=accountNumber #protected varaible _accountNumber
        self.__balance=balance #Private varaible __balance


    #getter method for balance
    def getBalance(self):
        return self.__balance
    
    #setter method for balance with validation

    def setBalance(self,newBalance):
        if(newBalance>=0):
            self.__balance=newBalance


    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    
    # public method withdraw the amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        
        else:
            print("Insuffient Balance..........")


account=BankAccount(4154442154,25000)
print(account.getBalance())  #25000
account.deposit(5000)
print(account.getBalance())  #30000
account.withdraw(7000)
print(account.getBalance()) #23000

print(account._accountNumber)
print(account._BankAccount__balance)