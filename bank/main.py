from bank_accounts import * 

checking = BankAccount(1000, "checking")
savings = BankAccount(2000, "savings")

checking.transfer(10000, savings)
savings.get_balance()
