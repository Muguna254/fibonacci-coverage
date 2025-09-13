import pytest
from fibonacci import fibonacci

def test_first_numbers():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)
