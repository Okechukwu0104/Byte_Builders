from decimal import Decimal

class Account:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = self.validate_balance(balance)

    def validate_balance(self , amount: Decimal):
        if amount < Decimal(0.00):
            return "Invalid balance"


