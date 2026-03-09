#encapsulation in python
class BankAccount:
    def __init__(self, balance):
        # Private variable
        self.__balance = balance
    # Getter 
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Invalid withdrawal amount")        
#object making
acc = BankAccount(1000)
#accessing balance 
print("Initial Balance:", acc.get_balance())
#depositing money
acc.deposit(500)
print("Balance after deposit:", acc.get_balance())
#withdrawing money
acc.withdraw(300)
print("Balance after withdrawal:", acc.get_balance())