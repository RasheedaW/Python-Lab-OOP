
# Task 3: Custom exception
class InsufficientFundsError(Exception):
    pass


# Task 1: BankAccount class
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: ${self.balance:.2f}"


# Task 2: SavingsAccount subclass
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=5):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

    def __str__(self):
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%"


# Test both account classes
if __name__ == "__main__":
    print("Bank Account Test")

    account = BankAccount("1001", "Jordan", 500)
    print(account)

    account.deposit(200)
    print("After deposit:", account)

    account.withdraw(100)
    print("After withdrawal:", account)

    # Test an invalid deposit
    try:
        account.deposit(-50)
    except ValueError as error:
        print("Error:", error)

    # Test insufficient funds
    try:
        account.withdraw(1000)
    except InsufficientFundsError as error:
        print("Error:", error)

    print("\nSavings Account Test")

    savings = SavingsAccount("2001", "Jordan", 1000, 5)

    savings.deposit(300)
    print("After deposit:", savings)

    savings.withdraw(100)
    print("After withdrawal:", savings)

    print("Before interest:", savings)
    savings.apply_interest()
    print("After interest:", savings)
