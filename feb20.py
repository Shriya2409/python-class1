"""Moderate Problem: Bank Account Management System
Problem Statement:
Design a class BankAccount with:
Class Attributes:
• bank_name = "National Bank"
• total_accounts = 0
• total_bank_balance = 0
Instance Attributes:
• account_holder
• balance
Requirements:
• Increment total_accounts when a new account is created.
• Add the initial deposit to total_bank_balance.
• Create methods:
• deposit(amount) → increase balance and update total_bank_balance
• withdraw(amount) → decrease balance and update total_bank_balance
• display_account_info()
• Ensure withdrawal cannot exceed balance.
In main function,
write menu driven operations."""

class BankAccount:
    """
    A class to represent a bank.
    class attributes: 
    bank_name(str): Name of the bank
    total_accounts(int): total number of accounts created
    total_bank_balance(float): total balance of all accounts combined
    """
    # Class Attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    # Constructor
    def __init__(self, account_holder: str, initial_deposit: float)->None:
        """
        Initialize a new bank account.
        args:
        account_holder(str): name of the account_holder
        initial_deposit(float): starting balance        
        """
        self.account_holder = account_holder
        self.balance = initial_deposit

        # Update class attributes
        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    # Deposit Method
    def deposit(self, amount: float)->None:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    # Withdraw Method
    def withdraw(self, amount: float)->None:
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw.
        """
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print("Withdrawal successful.")

    # Display Account Info
    def display_account_info(self)->None:
        """Display account details."""
        print("\n--- Account Information ---")
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Account Balance:", self.balance)
        print("----------------------------")


# Main Function
def main()->None:
    accounts = []

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Display Bank Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            deposit = float(input("Enter initial deposit: "))
            account = BankAccount(name, deposit)
            accounts.append(account)
            print("Account created successfully!")

        elif choice == "2":
            name = input("Enter account holder name: ")
            found = False
            for acc in accounts:
                if acc.account_holder == name:
                    amount = float(input("Enter deposit amount: "))
                    acc.deposit(amount)
                    found = True
                    break
            if not found:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account holder name: ")
            found = False
            for acc in accounts:
                if acc.account_holder == name:
                    amount = float(input("Enter withdrawal amount: "))
                    acc.withdraw(amount)
                    found = True
                    break
            if not found:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account holder name: ")
            found = False
            for acc in accounts:
                if acc.account_holder == name:
                    acc.display_account_info()
                    found = True
                    break
            if not found:
                print("Account not found.")

        elif choice == "5":
            print("\n--- Bank Summary ---")
            print("Total Accounts:", BankAccount.total_accounts)
            print("Total Bank Balance:", BankAccount.total_bank_balance)

        elif choice == "6":
            print("Thank you for using the Bank Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
