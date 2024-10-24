import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import unittest
from src.main import BankAccount, NegativeAmountError, InsufficientFundsError


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        self.wallet = BankAccount("josh", 1000.0)
        
    # test inital deposit
    def test_inital_deposit(self):
        self.assertEqual(self.wallet.balance, 1000.0)
        self.assertTrue(self.wallet.balance >= 0)
        
    # test deposit
    def test_deposit(self):
        self.wallet.deposit(500.0)
        self.assertEqual(self.wallet.balance, 1500.0)
        self.assertGreater(self.wallet.balance, 1000.0)
    
    # withdraw
    def test_withdraw(self):
        old_amount = self.wallet.balance
        self.wallet.withdraw(100.0)
        self.assertEqual(self.wallet.balance, 900.0)
        self.assertNotEqual(self.wallet.balance, old_amount)
    
    # insiffiencent funds
    def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.wallet.withdraw(10000.0)
    
    # negative deopist
    def test_neg_deposit(self):
        with self.assertRaises(NegativeAmountError):
            self.wallet.deposit(-150.0)

    
    # negatoive withdraw
    def test_neg_withdraw(self):
        with self.assertRaises(NegativeAmountError):
            self.wallet.withdraw(-100.0)
    
    # test account holder
    def test_account_holder(self):
        self.assertIsNotNone(self.wallet.account_holder)
        self.assertEqual(self.wallet.account_holder, "josh")
        
        
    def tearDown(self) -> None:
        self.wallet = None


if __name__ == "__main__":
    unittest.main()