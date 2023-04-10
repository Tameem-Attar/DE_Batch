import unittest 
class BankAccount:
    def __init__(self,account_num,account_type,pin):
        self.account_num=account_num 
        self.account_type=account_type 
        
        self.balance=0 
        
        if type(pin)==str:
            raise ValueError("PIN Must Be An Integer")
        elif pin>=1000 and pin<=9999:
            self.pin=pin 
            print("Your PIN Is Successfully Updated")     
        elif pin>=10000 or pin<1000:
            raise ValueError("PIN Must Be Four Digits") 
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount 
            return f"{amount} Successfully Added To Your Account"
        elif amount<=0:
            raise ValueError("Please Enter Some Valid Amount")
            
    def withdraw(self,amount):
        if amount<= self.balance and amount>0:
            self.balance-=amount 
            return f'Account Balance Updated {self.balance}' 
        elif amount<=0:
            return 'Please Enter A Positive Value'
        elif amount>self.balance:
            return 'Insufficient Funds' 
    def check_balance(self,pin):
        if pin==self.pin:
            return f"Your Account Balance Is {self.balance}"   
        else:
            raise ValueError("Your Pin Is Wrong. Please Enter A Valid Or Correct Pin") 



class Test_BankAccount(unittest.TestCase):
    
    def test_check_account_creation(self):
        with self.assertRaises(ValueError):
            self.account=BankAccount("2345678910","current","12") 
    
    def test_deposits(self):
        account=BankAccount("2345678910","savings",1234)
        self.assertEqual(account.deposit(2000),f"{2000} Successfully Added To Your Account")
        with self.assertRaises(ValueError):
            account.deposit(0) 

    def test_withdraws(self):
        account=BankAccount("2345678901","current",1234)
        self.assertEqual(account.withdraw(2000),"Insufficient Funds")
        self.assertEqual(account.withdraw(0),"Please Enter A Positive Value")
        print(account.deposit(2000))
        self.assertEqual(account.withdraw(1999),f"Account Balance Updated {account.balance}")
    
    
    def test_check_balance(self):
        account=BankAccount("2345678901","savings",1234) 
        print(account.deposit(20000)) 
        self.assertEqual(account.check_balance(1234),f'Your Account Balance Is {account.balance}') 
        with self.assertRaises(ValueError):
            account.check_balance(1235)
            account.check_balance("1234")



        
       
            
    
if __name__ == "__main__":
    unittest.main()



