class BankAccount:
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance

    def deposit(self,amount):
        return self.account_balance + amount
    
    def withdraw(self,amount):
        if amount >= 0 and amount <= self.account_balance:
            return True
        else:
            return False
    def display_balance(self):

        print(f"Current Balance: ${self.account_balance}")

    

if __name__ == "__main__":
    account = BankAccount(50)
    print(account.display_balance())
        
    