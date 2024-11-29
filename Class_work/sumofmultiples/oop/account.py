from decimal import Decimal
from card_number_generator import card_generator_function
class Account:
    def __init__(self, name: str, phone: str = "00000000000") -> None:
        self.name = name
        self.phone = self.set_phone(phone)
        self.balance = Decimal(0.00)
        self.credit_card = card_generator_function()

    def set_phone(self, phone: str):
        if len(phone) != 11:
            raise ValueError("Phone number must be 11 digits")
        self.phone = phone
        return self.phone

    def get_phone(self) -> str:
        return self.phone

    def validate_amount(self, amount: Decimal):
        if amount < Decimal(0.00):
            raise ValueError("Amount cannot be negative")

    def deposit(self, amount: Decimal):
        self.validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: Decimal):
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_card_number(self):
        return self.credit_card



