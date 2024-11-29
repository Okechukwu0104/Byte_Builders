import unittest
from decimal import Decimal
from account import Account

class TestAccount(unittest.TestCase):
    def test_that_account_exists(self):
        account1 = Account("Funmi", "08164699964")
        account2 = Account("Tobi", "08164699978")
        booku = Account("booku")

    def test_deposit_function_works(self):
        babatunde = Account("babatunde", "08164699968")
        self.assertEqual(babatunde.balance, Decimal(0.00))
        babatunde.deposit(Decimal(500.00))
        self.assertEqual(babatunde.balance, Decimal(500.00))

    def test_deposit_cannot_be_negative(self):
        babatunde = Account("babatunde", "08164699968")
        with self.assertRaises(ValueError):
            babatunde.deposit(Decimal(-500.00))

    def test_balance_after_deposit_and_withdrawal(self):
        babatunde = Account("babatunde", "08164699968")
        babatunde.deposit(Decimal(500.00))
        babatunde.withdraw(Decimal(400.00))
        self.assertEqual(babatunde.balance, Decimal(100.00))

    def test_withdrawal_exceeding_balance(self):
        babatunde = Account("babatunde", "08164699968")
        with self.assertRaises(ValueError):
            babatunde.withdraw(Decimal(1500.00))

    def test_withdrawal_cannot_be_negative(self):
        babatunde = Account("babatunde", "08164699968")
        with self.assertRaises(ValueError):
            babatunde.withdraw(Decimal(-500.00))


    def test_if_Creditcard_is_generated_on_account_creation(self):
        babatunde = Account("babatunde", "08164699968")
        self.assertEqual(len(babatunde.get_card_number()), 16)
