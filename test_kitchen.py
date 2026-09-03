# test_kitchen.py
from kitchen import Quantity

def test_multiply_quantity():
    q = Quantity(200, "g")
    result = q.times(3)
    assert result.amount == 600
    assert result.unit == "g"
def test_multiply_quantity_different_numbers():
    q = Quantity(10, "g")
    result = q.times(4)
    assert result.amount == 40
    assert result.unit == "g"
