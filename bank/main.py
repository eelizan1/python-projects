from bank_accounts import * 
from interest_rewards_account import InterestRewardsAccount 

checking = BankAccount(1000, "checking")
savings = BankAccount(2000, "savings")

checking.transfer(10000, savings)
savings.get_balance()

interest_rewards_acct = InterestRewardsAccount(300, 'Interest Rewards Account')
interest_rewards_acct.deposit(400)

interest_rewards_acct.transfer(700, savings)
interest_rewards_acct.get_balance()