class BankAccount():

    all_accounts = []
    
    def __init__(self, int_rate = 0.01, balance = 0,):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)
        return cls


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(0.02, 0)
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
link = User("Link from Zelda", "link@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(150).display_user_balance()
monty.make_deposit(250).make_deposit(575).make_withdrawal(28).make_withdrawal(49).display_user_balance()
link.make_deposit(1000).make_withdrawal(323).make_withdrawal(29).make_withdrawal(135).display_user_balance()
guido.transfer_money(link, 125).display_user_balance()
link.display_user_balance()
