#C06_EX03: Scrieti o clasa Account (fields: iban: str, owner: str, balance: float -> default 0).
# Metode:
# - show_balance() - "<owner> are in contul <iban> suma de <balance> RON"
# - withdraw(amount)
# - deposit(amonut)

class Account:
    def __init__(self, iban, owner, balance=0.0):
        self.iban = iban
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f'{self.owner} are in contul {self.iban} suma de {self.balance} RON')

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance -= amount
        return amount

new_account = Account("ROON1234XYZ", "Mihai")
print(new_account.balance)
new_account.show_balance()
new_account.deposit(5000)
new_account.show_balance()
new_account.deposit(1000)
withdraw_amount = new_account.withdraw(2500)
print(withdraw_amount)
new_account.show_balance()
withdraw_amount = new_account.withdraw(4000)






