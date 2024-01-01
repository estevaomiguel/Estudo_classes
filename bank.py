class BankAccount:
    def __init__(self, accountNumber, f_name, l_name, balance):
        self.accountNumber = accountNumber
        self.f_name = f_name
        self.l_name = l_name
        self.balance = balance

    def Deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def Withdrawal(self, amount):
        self.balance = self.balance - amount
        return

    def Welcoming(self):
        return f"Hello {self.f_name} {self.l_name}, welcome to our bank"

    @property
    def email(self):
        email = f"{self.f_name}.{self.l_name}@gmail.com"
        return email

    @email.setter
    def email(self, new_email):
        name = new_email.split("@")






