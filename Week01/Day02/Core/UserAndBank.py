class BankAccount:
    agency = " "
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

        BankAccount.all_account = self
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} added successfully")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Sorry not enough money")
        else:
            self.balance -= amount
            print("Your new balance is",self.balance)
        return self

    def display_account_info(self):
        print(f"The rate of this account is {self.rate} so your balance for now {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def start(self, amount):
        self.account.deposit(amount)

    def retreve(self, amount):
        self.account.withdraw(amount)

    def my_balance(self):
        self.account.display_account_info()


acc1 = User("med", "@gmail")
acc1.start(100)
acc1.retreve(200)
info = acc1.my_balance()
print (info)