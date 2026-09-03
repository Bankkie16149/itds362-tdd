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
def test_times_does_not_mutate_original():
    original = Quantity(200, "g")
    result = original.times(3)
    assert original.amount == 200      # ต้นฉบับต้องไม่เปลี่ยน
    assert result.amount == 600
def test_quantities_with_same_amount_are_equal():
    assert Quantity(200, "g") == Quantity(200, "g")
