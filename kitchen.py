# kitchen.py
class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)
    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def plus(self, other):
        if self.unit == other.unit:
            return Quantity(self.amount + other.amount, self.unit)
        else:
            raise ValueError("Units do not match")
