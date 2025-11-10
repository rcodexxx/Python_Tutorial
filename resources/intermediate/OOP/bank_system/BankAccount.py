"""
基本類別：銀行帳戶（BankAccount）
建立一個「銀行帳戶」類別，它有以下特點：

屬性：帳戶持有人（owner）、餘額（balance）
方法：存款（deposit）、提款（withdraw）、查詢餘額（get_balance）
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 用雙底線 "__" 表示私有屬性

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount} 元，新餘額為 {self.__balance} 元")
        else:
            print("存款金額必須大於 0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount} 元，新餘額為 {self.__balance} 元")
        else:
            print("提款金額無效")

    def get_balance(self):
        return self.__balance