import unittest
from oopRecord import Account
import Decimal




class TestRecord(unittest.TestCase):
    def test_record(self):
        account1 = Account("tijani","080992334581","120000")

    def test_that_balance_cant_be_a_negative_amount(self):
        account1 = Account("tijani","080992334581","-120000")
        self.assertEqual(account1,"Invalid Balance")

    def test_that_account_can_deposit(self):
        account1 = Account("tijani","09884923491", 1000)

