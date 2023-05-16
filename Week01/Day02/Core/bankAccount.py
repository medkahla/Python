class BankAccount:
    agency = " "
    all_account = []
    def __init__(self, int_rate, balance): 
        self.rate = int_rate
        self.balance = balance

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

acc1 = BankAccount(0.26,0)
acc2 = BankAccount(0.29,0)
acc1.deposit(100).deposit(80).deposit(50).withdraw(100).yield_interest().display_account_info()
acc2.deposit(110.6).deposit(48.5).withdraw(200).yield_interest().display_account_info()