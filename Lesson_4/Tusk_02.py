class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.history = []  # Список для хранения истории операций

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposit: {amount}")
            return f"Successfully deposited: {amount}. New balance: {self.balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw: {amount}")
            return f"Successfully withdrew: {amount}. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            return "Withdrawal amount must be greater than zero."

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def get_history(self):
        return self.history

# Пример использования
atm = ATM(100)  # Начальный баланс 100
print(atm.deposit(50))  # Депозит 50
print(atm.withdraw(30))  # Снятие 30
print(atm.withdraw(150))  # Попытка снятия 150 (недостаточно средств)
print(atm.get_balance())  # Проверка баланса
print("История операций:", atm.get_history())  # Проверка истории операций
