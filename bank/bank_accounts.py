from BalanceException import * 

class BankAccount: 
    def __init__(self, initial_amount, acct_name): 
        # "account_balance" and "account_name" are instance variables created 'on the fly' in the init
        self.account_balance = initial_amount
        self.account_name = acct_name
        print(f"\nAccount '{self.account_name}' created. \nBalance = ${self.account_balance:.2f}")

    def get_balance(self): 
        print(f"\nAccount '{self.account_name}' has a balance of ${self.account_balance:.2f}")
        return self.account_balance

    def deposit(self, amount): 
        self.account_balance = self.account_balance + amount
        print(f"\nDeposit complete")
        return self.get_balance()
    
    def withdraw(self, amount): 
        # use try catch since viable_transaction could throw an exception 
        try: 
            self.viable_transaction(amount)
            self.account_balance = self.account_balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}') 

    def viable_transaction(self, amount): 
        if self.account_balance >= amount: 
            return
        else: 
            raise BalanceException(
                f"\nSorry, account '{self.account_name} only has a balance of ${self.account_balance:.2f}'"
            )
    
    def transfer(self, amount, account): 
        try: 
            print('\n**********\n\n Beginning Transfer...')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete!\n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted. {error}')