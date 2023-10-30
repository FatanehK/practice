'''Implement a banking system with different account types.
Description: You are tasked with creating a banking system.
 Design a system to support different account types. 
 The system should support different account types such as `Savings Account`, 
 `Checking Account`, and `Loan Account` (we might need to add more account types in future).
 Each account should have attributes for the account number,
balance, and account type-specific features. Create a class Bank that manages customer accounts.

Usage Example:

(This example is in python, but you can use any language you prefer)

 

# Create a bank

bank = Bank()

 

# Create accounts

savings_account = SavingsAccount("SA123", 1000)

checking_account = CheckingAccount("CA456", 500)

loan_account = LoanAccount("LA789", 5000)

 

# Deposit and withdraw from accounts

savings_account.deposit(500)  # Savings Account balance: 1000 + 500 = 1500

checking_account.withdraw(200)  # Checking Account balance: 500 - 200 = 300

loan_account.withdraw(1000)  # Loan Account balance (loan amount): 5000 - 1000 = 4000

 

# Transfer money between accounts

bank.transfer(savings_account, checking_account, 200)

# Transfer: $200 from Savings Account to Checking Account

# After transfer: Savings Account balance: 1500 - 200 = 1300, Checking Account balance: 300 + 200 = 500

 

# Display account information

print(f"Savings Account ({savings_account.get_account_number()}): Balance ${savings_account.get_balance()}")

# Output: Savings Account (SA123): Balance $1300

 

print(f"Checking Account ({checking_account.get_account_number()}): Balance ${checking_account.get_balance()}")

# Output: Checking Account (CA456): Balance $500

 

print(f"Loan Account ({loan_account.get_account_number()}): Remaining Loan Amount ${loan_account.calculate_remaining_loan()}")

# Output: Loan Account (LA789): Remaining Loan Amount $4000



'''
class Bank:
    def __init__(self) -> None:
        self.accounts=[]

    def create_account(self,account):
        self.accounts.append(account)
    def transfer(self,from_acc_number,to_acc_number,amount):

class Account:
    def __init__(self,account_number,balance) -> None:
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    

class CheckingAccount(Account):
    def __init__(self,account_number,balance):
        super().__init__(account_number, balance)


class SavingsAccount(Account):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)

class LoanAccount(Account):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)

    def calculate_remaining_loan(self):
        return self.balance


bank = Bank()

savings_account = SavingsAccount("SA123", 1000)
checking_account = CheckingAccount("CA456", 500)
loan_account = LoanAccount("LA789", 5000)

bank.create_account(savings_account)
bank.create_account(checking_account)
bank.create_account(loan_account)


savings_account.deposit(500)  # Savings Account balance: 1000 + 500 = 1500
checking_account.withdraw(200)  # Checking Account balance: 500 - 200 = 300
checking_account.deposit(1000000)
loan_account.withdraw(1000)
print(
    f"Savings Account ({savings_account.get_account_number()}): Balance ${savings_account.get_balance()}")

# Output: Savings Account (SA123): Balance $1300

print(
    f"Checking Aaccount({checking_account.get_account_number()}):Balance ${checking_account.get_balance()} ")

print(f"Loan Account ({loan_account.get_account_number()}): Remaining Loan Amount ${loan_account.calculate_remaining_loan()}")
