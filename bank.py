class BankAccount:

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your new balance with the deposit is {self.balance}" )

    def Withdrawal(self, amount):
        self.balance = self.balance - amount
        if self.balance >= 0:
             print(f"Your new balance with the withdrawal is {self.balance}" )
        else:
            raise Exception("The transaction is not possible due to lack of funds")

    def BankFees(self):
        fee = self.balance * 0.05
        self.balance = self.balance - fee

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

new_account = BankAccount(2178514584, "Miguel", 2700)

new_account.Withdrawal(300)
new_account.display()
