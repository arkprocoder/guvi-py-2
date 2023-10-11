'''
Problem: Create a Class for a Simple Bank Account

You are tasked with creating a Python class that represents a simple bank account. The class should have the following attributes and methods:

Attributes:

account_number (a unique string to identify the account)
account_holder_name (string, the name of the account holder)
balance (a floating-point number, representing the current account balance)
Methods:

A constructor method (__init__) that initializes the account with an account number and an account holder's name. The initial balance should be set to 0.0.

A deposit method that takes an amount as a parameter and adds it to the account balance.

A withdraw method that takes an amount as a parameter and subtracts it from the account balance. Make sure the account has sufficient funds for the withdrawal. If not, display an error message.

A get_balance method that returns the current account balance.

A display_account_info method that displays the account number, account holder's name, and current balance.

Create an instance of the class and demonstrate its functionality by depositing and withdrawing money, displaying the account information, and checking for errors.

Example:

python
Copy code
# Create a bank account
my_account = BankAccount("123456", "John Doe")

# Deposit $500
my_account.deposit(500)

# Withdraw $200
my_account.withdraw(200)

# Display account information
my_account.display_account_info()
# Output should be:
# Account Number: 123456
# Account Holder: John Doe
# Balance: $300.0

# Try to withdraw an amount greater than the balance
my_account.withdraw(400)
# Output should be an error message.

# Display the balance
balance = my_account.get_balance()
# balance should be 300.0


'''