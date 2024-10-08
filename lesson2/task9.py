from __future__ import annotations


class BankAccount:
    def __init__(self,balance: float,) -> None:
        if balance <0:
            raise ValueError(' Баланс не может быть отрицательным ')
        self.__balance : int = balance

    def deposit(self, amount: float): 
        if amount < 0:
            raise ValueError(' Депозит не может быть отрицательным')
        self.__balance += amount

        
    def withdraw(self, amount : float):
        if not self.__balance >= amount > 0:
          raise ValueError(' Вы не можете снять меньше 0 или больше чем у вас на счету')
        self.__balance -= amount
         
 
    

    def get_balance(self):
        return self.__balance





    def __str__(self) -> str:
        return f'На счету - {self.__balance}'

account = BankAccount(balance=1000)
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())

