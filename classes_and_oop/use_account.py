from account import Account
from classes_and_oop.account import BusinessAccount

some_account = Account(1000.00)

some_account.deposit(550.23)
some_account.deposit(100)
some_account.withdraw(50)

print("New balance", some_account.balance)
print(some_account)

another_account = Account(0)
print("Total accounts created", Account.get_num_accounts())
print("object another_account is of type", another_account.__class__.__name__)
print(another_account)


bzns = BusinessAccount(50000)
print("object bzns is of type", bzns.__class__.__name__)
print(bzns)

bzns2 = BusinessAccount(20000)
print(bzns, bzns2)

bzns.transfer(bzns2)
print(bzns, bzns2)

bzns3 = BusinessAccount(30000)
account3 = Account(0)
print("Total accounts created", Account.get_num_accounts())
print("Total business accounts created", BusinessAccount.get_num_accounts())

# operator overloading
print("sum accounts: ", bzns + bzns2)