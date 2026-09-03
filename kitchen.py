# kitchen.py
class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        self.amount = self.amount * multiplier       
        return self
