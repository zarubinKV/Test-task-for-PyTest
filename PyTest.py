import pytest
import math as m
import ipytest

ipytest.autoconfig()

#tests for int

def test_type_int():
    assert type(5) == int
    
def test_integer_division():
    assert (10 // 4) == 2
    
def test_sqrt_int():
    try:
        assert m.sqrt(-1) == complex(0, 1)
    except ValueError:
        pass

#tests for float

def test_is_float():
    assert float.is_integer(5.5) == False
    
def test_int_to_float():
    assert float(10) == 10.0 and type(float(10)) == float

@pytest.mark.parametrize("x, y, expected", [(2.4, 3.7, 8.88), (1.7, 0.0, 0.0), (-1.3, -1.7, 2.21), (12.7, -1.6, -20.32)])
def test(x, y, expected):
    assert x * y == expected
    
ipytest.run()
