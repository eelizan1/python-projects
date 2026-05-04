from bank_accounts import BankAccount


# class inheritance - InterestRewardsAccount is a child class that inherits from BankAccount 
class InterestRewardsAccount(BankAccount): 
    # overrides depoist from parent to have its own deposit since that would be the ONLY difference between the two classes 
    def deposit(self, amount): 
        self.account_balance = self.account_balance + (amount * 1.05)
        print("\nRewards account deposit complete")
        self.get_balance()