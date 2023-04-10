class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
      self.account_number = account_number
      self.account_holder_name = account_holder_name
      self.account_balance = account_balance

    def deposit(self, amount):
      self.account_balance += amount
      print(f"Deposit of {amount} successful. New balance is {self.account_balance}")

    def withdraw(self, amount):
      if amount > self.account_balance:
          print("Insufficient funds. Withdrawal unsuccessful.")
      else:
           self.account_balance -= amount
           print(f"Withdrawal of {amount} successful. New balance is {self.account_balance}")

    def display_balance(self):
        print(f"Current balance is {self.account_balance}")
        

class TestBankAccount:

    def test_deposit(self):

        account = BankAccount(123456, "John Smith", 1000.0)
        account.deposit(500.0)
        assert account.account_balance == 1500.0


    def test_withdraw_sufficient_funds(self):

        account = BankAccount(123456, "John Smith", 1000.0)
        account.withdraw(500.0)
        assert account.account_balance == 500.0


    def test_withdraw_insufficient_funds(self):

        account = BankAccount(123456, "John Smith", 1000.0)
        account.withdraw(1500.0)
        assert account.account_balance == 1000.0


    def test_display_balance(self):

        account = BankAccount(123456, "John Smith", 1000.0)
        try:
         assert account.display_balance() ==  1000.0
        except AssertionError:
           print("Error in Asserting the values")

test_bank_account = TestBankAccount()
test_bank_account.test_deposit()
test_bank_account.test_withdraw_sufficient_funds()
test_bank_account.test_withdraw_insufficient_funds()
test_bank_account.test_display_balance()

