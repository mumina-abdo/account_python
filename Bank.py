class Account:
    def __init__(self, number, pin, owner_name="Unknown"):
        self.number = number
        self.__pin = pin
        self.__owner_name = owner_name
        self.__balance = 0
        self.__overdraft_limit = None
        self.__minimum_balance = None
        self.__is_frozen = False
        self.__transaction_history = []
    def view_account_details(self, pin):
        if pin == self.__pin:
            return {f"Account Number": {self.number},"Owner Name": {self.__owner_name},"Current Balance": {self.__balance}}
        else:
            return "Wrong PIN"
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient balance")
    def change_account_owner(self, new_owner_name, pin):
        if pin == self.__pin:
            self.__owner_name = new_owner_name
            return f"Account owner changed to {new_owner_name}."
        else:
            return "Wrong PIN"
    def account_statement(self, pin):
        if pin == self.__pin:
            # transactions = ["Deposit $800", "Withdrawal $100"]
            return self.__transaction_history
        else:
            return "Wrong PIN"
    def set_overdraft_limit(self, limit, pin):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return f"Overdraft limit set to ${limit}."
        else:
            return "Wrong PIN"
    def calculate_interest(self, rate, pin):
        if pin == self.__pin:
            interest_amount = self.__balance * rate / 100
            self.__balance += interest_amount
            return f"Interest calculated. New balance: ${self.__balance}"
        else:
            return "Wrong PIN"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account frozen."
        else:
            return "Wrong PIN"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account unfrozen."
        else:
            return "Wrong PIN"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return self.__transaction_history
        else:
            return "Wrong PIN"
    def set_minimum_balance(self, min_balance, pin):
        if pin == self.__pin:
            self.__minimum_balance = min_balance
            return f"Minimum balance requirement set to ${min_balance}."
        else:
            return "Wrong PIN"
    def transfer_funds(self, amount, recipient_number, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawal: ${amount} to {recipient_number}")
                return f"Funds transferred successfully. New balance: ${self.__balance}"
            else:
                return "Insufficient funds."
        else:
            return "Wrong PIN"
    def close_account(self, pin):
        if pin == self.__pin:
            return "Account closed."
my_account = Account(number="100025", pin=5678)
print(my_account.view_account_details(5678))
print(my_account.deposit(30000))
print(my_account.withdraw(5000))
print(my_account.change_account_owner("Abdirizack Abdo",5678 ))
print(my_account.account_statement(5678))
print(my_account.set_overdraft_limit(200000, 5678))
print(my_account.calculate_interest( 3, 5678))
print(my_account.freeze_account(5678))
print(my_account.unfreeze_account(5678))
print(my_account.transaction_history(5678))
print(my_account.set_minimum_balance( 6000, 5678))
print(my_account.transfer_funds(40000, 789012, 5678))
print(my_account.close_account(456))












