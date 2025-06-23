# test_factorial.py

from factorial import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1
    assert factorial(0) == 1
