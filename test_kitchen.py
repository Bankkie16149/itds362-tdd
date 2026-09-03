# test_kitchen.py
from kitchen import Quantity

def test_multiply_quantity():
    q = Quantity(200, "g")
    result = q.times(3)
    assert result.amount == 600
    assert result.unit == "g"
