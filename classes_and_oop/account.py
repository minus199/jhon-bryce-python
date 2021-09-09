class Account:
    __numCreated = 0

    def __init__(self, initial_balance, account_type="personal"):
        self.account_type = account_type
        self.__balance = initial_balance
        Account.__numCreated += 1
        self.__id = Account.__numCreated
    def deposit(self, amt):
        self.__balance = self.__balance + amt
        return self.balance

    def withdraw(self, amt):
        self.__balance = self.__balance - amt
        return self.balance

    def _reset_account(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        pass

    # (+) plus operator overloading
    # def __add__(self, other):
    #     return self.balance + other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __str__(self):
        return f'Account {self.__id} [current amount {self.balance}]'

    def __repr__(self):
        return f'{self.account_type.title()} Account - Id: {self.__id} [current amount {self.balance}]'
    @classmethod
    def get_num_accounts(cls):
        return cls.__numCreated
x = Account(1)
print()
class BusinessAccount(Account):
    def transfer(self, account):
        account.deposit(self.balance)
        self._reset_account()
        # return self.__balance # will not work, it is private
        return self.balance

    def __str__(self):
        return "Business {0}".format(super(BusinessAccount, self).__str__())


class StudentAccount(Account):
    pass
