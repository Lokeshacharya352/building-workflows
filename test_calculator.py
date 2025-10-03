import pytest
from calculator import add, subtract, multiply, divide, power, sqrt

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):  # check division by zero
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_sqrt():
    assert sqrt(16) == 4
    with pytest.raises(ValueError):  # check sqrt of negative number
        sqrt(-9)
