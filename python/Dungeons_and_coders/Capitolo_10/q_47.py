'''
Nel laboratorio occorre un conto per reagenti preziosi. Che la procedura lo dichiari: `BankAccount` con `balance` opzionale, `deposit(amount)` che aumenta e `withdraw(amount)` che riduce o solleva **`ValueError`** se il saldo non basta. Mantieni la firma data e fai superare tutti i test automatici.
'''

class BankAccount:
    
    def __init__(self, balance = 0) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if self.balance - amount < 0:
            raise ValueError
        else:
            self.balance -= amount