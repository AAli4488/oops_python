# banking_interest_system.py

class Account:
    def __init__(self, balance):
        self._balance = balance

    def calculate_interest(self):
        raise NotImplementedError


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.04 if self._balance <= 50000 else self._balance * 0.06


class FixedDepositAccount(Account):
    def __init__(self, balance, years):
        super().__init__(balance)
        self.years = years

    def calculate_interest(self):
        return self._balance * 0.07 * self.years


class LoanAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.10


# Main
print("---- Banking Interest System ----")
print("1. Savings Account")
print("2. Fixed Deposit")
print("3. Loan Account")

choice = input("Choose account type: ")
balance = float(input("Enter balance: "))

if choice == "1":
    acc = SavingsAccount(balance)
elif choice == "2":
    years = int(input("Enter years: "))
    acc = FixedDepositAccount(balance, years)
elif choice == "3":
    acc = LoanAccount(balance)
else:
    print("Invalid choice")
    exit()

print("Calculated Interest:", acc.calculate_interest())
