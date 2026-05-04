from balance_exception import BalanceException
from interest_rewards_account import InterestRewardsAccount


class SavingsAccount(InterestRewardsAccount): 
    def __init__(self, initial_amount, account_name): 
         super().__init__(initial_amount, account_name)
         self.fee = 5 # fee for any withdraw from this account 

    def withdraw(self, amount):
        try: 
            self.viable_transaction(amount + self.fee)
            self.account_balance = self.account_balance - (amount + self.fee)
            self.get_balance()
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')