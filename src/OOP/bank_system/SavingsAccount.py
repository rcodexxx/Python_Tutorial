from src.OOP.bank_system.BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)  # 呼叫父類的初始化
        self.interest_rate = interest_rate  # 利息率

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"新增利息 {interest} 元")