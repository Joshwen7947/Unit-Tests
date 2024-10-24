import logging

logging.basicConfig(level=logging.INFO)

class BankAccountError(Exception):
    """Base class for exceptions in the bank account module."""
    pass

class NegativeAmountError(BankAccountError):
    """Exception raised for negative amounts."""
    pass

class InsufficientFundsError(BankAccountError):
    """Exception raised when trying to withdraw more than the balance."""
    pass

class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive")
        self._balance += amount
        logging.info(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self._balance -= amount
        logging.info(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self) -> str:
        return f"Account holder: {self.account_holder}, Balance: {self.balance}"


wallet = BankAccount("josh",25000)
wallet.withdraw(500)