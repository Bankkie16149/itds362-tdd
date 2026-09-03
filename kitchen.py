CONVERSION_RATES = {
    ("oz", "g"): 28.3495,
    ("g", "oz"): 1 / 28.3495,
}

class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, target_unit):
        if self.unit == target_unit:
            return self
        rate = CONVERSION_RATES[(self.unit, target_unit)]
        return Quantity(self.amount * rate, target_unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, target_unit):
        left_converted = self.left.reduce(target_unit)
        right_converted = self.right.reduce(target_unit)
        return Quantity(left_converted.amount + right_converted.amount, target_unit)

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))